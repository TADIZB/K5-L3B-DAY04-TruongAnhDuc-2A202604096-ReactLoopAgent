# Ghi chú phân tích · Day 04

Họ và tên: Trương Anh Đức
MSSV: 2A202604096

## 1. Case được chọn

- ID case: H6
- Câu trả lời của agent: Agent nêu rằng incident h02n9572mx9y có liên kết tới incident tổng hợp có thể chứa nguyên nhân, nhưng không mở liên kết để xác nhận; câu trả lời không nêu nguyên nhân/ảnh hưởng cụ thể từ summary đó.
- Điểm ở lần chạy 1: 55/100

## 2. Bằng chứng trong trace

Dấu vết trong `eval_before.json`: ở step 1, `get_incident_details` cho `h02n9572mx9y` trả update resolved có URL `https://www.githubstatus.com/incidents/xr3myzj7ms51`. Sau đó trace chuyển thẳng sang model step 2 với `finish: stop`, không có tool event đọc incident `xr3myzj7ms51`. Nguyên nhân có thể là system prompt chưa nhắc agent theo các liên kết incident liên quan khi câu hỏi yêu cầu.

```json
{"event":"tool","step":1,"name":"get_incident_details","arguments":{"provider":"github","incident_id":"h02n9572mx9y"},"result":{"updates":[{"status":"resolved","body":"Please refer to the combined summary in this related incident: https://www.githubstatus.com/incidents/xr3myzj7ms51"}],"url":"https://stspg.io/7pwv28hvkmz8"}}
{"event":"model","step":2,"finish":"stop","tool_calls":[]}
```

## 3. Thay đổi đã thực hiện

- Sửa gì, ở đâu: Trong `agent.py`, bổ sung hướng dẫn cho linked incident; với yêu cầu theo link/tìm nguyên nhân, tự đọc tối đa bốn incident liên quan mỗi model step và ghi tool call vào trace. Cập nhật kiểm tra nguồn để một lần sửa yêu cầu tất cả URL incident đã quan sát cùng lúc.
- Vì sao chọn thay đổi này: H6 yêu cầu rõ “theo liên kết”. Trace baseline cho thấy agent dừng sau khi thấy URL; lần eval đầu sau cải tiến phát hiện thêm vòng lặp khi model được yêu cầu bổ sung nhiều URL nguồn riêng rẽ.

## 4. So sánh hai lần chạy

| Chỉ số | `eval_before.json` | `eval_after.json` |
|---|---|---|
| Điểm tổng | 80.18/100 | 80.23/100 |
| Điểm case đã chọn | 55/100 (H6) | 60/100 (H6) |
| Số model calls | 72 (50 agent + 22 judge) | 71 (49 agent + 22 judge) |
| Token, chi phí nếu có | 91,628 tokens; $0.019585 | 88,878 tokens; $0.018437 |

- Lỗi đã giải quyết: H6 hiện gọi `get_incident_details` cho linked incident `xr3myzj7ms51`; câu trả lời nêu được nguyên nhân từ combined summary và cả hai URL nguồn. Điểm H6 tăng 5 điểm.
- Lỗi còn lại hoặc mới xuất hiện: điểm tổng chỉ tăng nhẹ (0.05); H6 vẫn được judge đánh giá còn thiếu một số chi tiết. Các điểm judge dao động giữa lần chạy và một lần chạy mỗi phiên bản chưa chứng minh độ ổn định.

## 5. Giới hạn

Điểm judge là ước lượng và có thể nhầm; snapshot là dữ liệu cố định tại thời điểm thu thập, không phản ánh status live; một lần chạy mỗi phiên bản chưa chứng minh độ ổn định.
