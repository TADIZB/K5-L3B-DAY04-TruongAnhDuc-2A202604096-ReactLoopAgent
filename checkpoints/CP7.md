# CP7 · Demo và nộp bài

**Mục tiêu:** trình bày agent, kết quả và giới hạn; nộp repo đúng yêu cầu.

**Trạng thái trong repo này:** tài liệu CP1–CP7, agent, hai eval hợp lệ, NOTES và tests đã sẵn. Demo, push repo public và nộp link LMS cần bạn thực hiện trong tài khoản cá nhân.

## Demo

1. Trình bày một trace có nhiều bước: status lookup, incident details và câu trả lời cuối có nguồn.
2. Nêu một lỗi agent đã thấy trong eval, bằng chứng trong trace và thay đổi đã thực hiện.
3. So sánh kết quả trước/sau, đồng thời nói rõ judge là ước lượng và snapshot phản ánh dữ liệu tại thời điểm được lưu.

## Checklist nộp

- [ ] Có `agent.py`, `eval_before.json`, `eval_after.json`, `NOTES.md` và các file dự án còn lại.
- [ ] Cả hai eval có đủ 22 case được chấm; điểm tổng không phải `null`.
- [ ] `NOTES.md` đủ 5 mục.
- [ ] `python -m unittest discover -s tests -v` không còn test lỗi.
- [ ] Repo không chứa `.env` hay API key; chỉ giữ `.env.example`.
- [ ] Tên repo theo lớp, họ tên không dấu và MSSV; repo public và mở được khi chưa đăng nhập.
- [ ] Đã nộp link repo lên bài Day 04 trên LMS trước hạn áp dụng cho ca học.

Nếu làm bonus, nộp thêm `eval_bonus.json` và ghi chú retry, pagination, context cùng giới hạn còn lại.
