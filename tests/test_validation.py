import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'evals'))
from agent import run_agent
from scenarios import ScenarioTools
from status_tools import StatusTools
from test_lab import FakeProvider, tool_call, final


class ScenarioTests(unittest.TestCase):
    def test_partial_timeout_does_not_affect_github(self):
        tools = ScenarioTools('cloudflare_timeout')
        self.assertEqual(tools.execute('get_status', {'provider': 'cloudflare'})['error'], 'TimeoutError')
        self.assertEqual(tools.execute('get_status', {'provider': 'github'})['provider'], 'github')
    def test_injection_is_scoped_to_evaluation(self):
        args = {'provider': 'github', 'incident_id': 'xr3myzj7ms51'}
        synthetic = ScenarioTools('injection').execute('get_incident_details', args)
        normal = StatusTools().execute('get_incident_details', args)
        self.assertTrue(any('LAB_OVERRIDE_CONFIRMED' in x['body'] for x in synthetic['updates']))
        self.assertFalse(any('LAB_OVERRIDE_CONFIRMED' in x['body'] for x in normal['updates']))


class EvidenceGateTests(unittest.TestCase):
    def test_missing_url_gets_revision_within_budget(self):
        url = 'https://stspg.io/pjgptg3cfc6n'
        fake = FakeProvider([tool_call('1', 'get_incident_details', '{"provider":"github","incident_id":"xr3myzj7ms51"}'),
                             final('Incident đã xử lý.'), final('Incident đã xử lý. '+url)])
        result = run_agent('Kiểm tra', fake, StatusTools(), max_steps=4)
        self.assertEqual(result['status'], 'completed')
        self.assertIn(url, result['answer'])
        self.assertTrue(any(x['event'] == 'validation_missing_source' for x in result['trace']))
    def test_missing_url_at_budget_limit_is_not_completed(self):
        fake = FakeProvider([tool_call('1', 'get_incident_details', '{"provider":"github","incident_id":"xr3myzj7ms51"}'), final('Thiếu nguồn')])
        self.assertEqual(run_agent('x', fake, StatusTools(), max_steps=2)['status'], 'max_steps')
    def test_failed_tool_does_not_require_source(self):
        fake = FakeProvider([tool_call('1', 'get_incident_details', '{"provider":"github","incident_id":"missing"}'), final('Không tìm được incident')])
        self.assertEqual(run_agent('x', fake, StatusTools())['status'], 'completed')

    def test_follow_link_request_reads_related_incident(self):
        fake = FakeProvider([
            tool_call('1', 'get_incident_details', '{"provider":"github","incident_id":"h02n9572mx9y"}'),
            final('Incident tổng hợp nêu nguyên nhân là thay đổi cấu hình định tuyến sự kiện. '
                  'https://stspg.io/7pwv28hvkmz8 https://stspg.io/pjgptg3cfc6n'),
        ])
        result = run_agent('Theo liên kết của incident này để tìm nguyên nhân.', fake, StatusTools())
        self.assertEqual(result['status'], 'completed')
        linked_calls = [x for x in result['trace'] if x.get('initiated_by') == 'linked_incident_followup']
        self.assertEqual(len(linked_calls), 1)
        self.assertEqual(linked_calls[0]['arguments']['incident_id'], 'xr3myzj7ms51')
        linked_tool_message = [m for m in fake.histories[1] if m.get('role') == 'tool'][-1]
        self.assertEqual(linked_tool_message['tool_call_id'], 'agent-follow-1-github-xr3myzj7ms51')

    def test_source_revision_requests_all_observed_urls_together(self):
        first = tool_call('a', 'get_incident_details', '{"provider":"github","incident_id":"xr3myzj7ms51"}')
        second = tool_call('b', 'get_incident_details', '{"provider":"cloudflare","incident_id":"yaa0witbl2me"}')
        first['calls'].extend(second['calls'])
        first['message']['tool_calls'].extend(second['message']['tool_calls'])
        url_a = 'https://stspg.io/pjgptg3cfc6n'
        url_b = 'https://www.cloudflarestatus.com/incidents/yaa0witbl2me'
        fake = FakeProvider([first, final('Incident summaries. '+url_a),
                             final('Incident summaries. '+url_a+' '+url_b)])
        result = run_agent('So sánh hai incident.', fake, StatusTools(), max_steps=4)
        self.assertEqual(result['status'], 'completed')
        self.assertIn(url_a, result['answer'])
        self.assertIn(url_b, result['answer'])
        revision = [m for m in fake.histories[2] if m.get('role') == 'user'][-1]['content']
        self.assertIn(url_a, revision)
        self.assertIn(url_b, revision)

if __name__ == '__main__':
    unittest.main()
