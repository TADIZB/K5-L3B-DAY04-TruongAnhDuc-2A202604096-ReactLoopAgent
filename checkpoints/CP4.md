# CP4 · Eval lần 1

**Mục tiêu:** tạo baseline đầy đủ 22 case từ cùng bộ snapshot.

## Các bước

1. Xác nhận `PROVIDER`, `MODEL` và biến API key tương ứng hoạt động. Có thể đặt cấu hình trong `.env`, nhưng phải nạp các biến vào terminal trước khi chạy.
2. Chạy:

   ```powershell
   python evals/run_evals.py --output eval_before.json
   ```

3. Mở `eval_before.json`; đọc `summary`, `grade.reason`, `grade.mechanical`, câu trả lời và trace của từng case.
4. Nếu có case `unscored`, xử lý lỗi provider/judge rồi chạy lại. Không dùng `partial_mean_0_100` thay điểm tổng.
5. Chọn case điểm thấp hoặc lỗi trong trace để phân tích ở CP5.

## Hoàn thành khi

- Có đủ 22 case E1–E6, A1–A8, H1–H8.
- `summary.score_0_100` khác `null`; tất cả case được chấm.
- Cấu hình model và giới hạn bước được ghi nhận để tái sử dụng ở CP6.

Eval gọi model và judge thật, nên có thể dùng quota API. Không đưa key vào trace hoặc file nộp.

**Trạng thái trong repo này:** hoàn thành với OpenRouter model `openai/gpt-4o-mini`: đủ 22/22 case được chấm, tổng 80.18/100. Những lần chạy Gemini bị 429 và model OpenRouter trước đó bị 404 không được dùng làm baseline.
