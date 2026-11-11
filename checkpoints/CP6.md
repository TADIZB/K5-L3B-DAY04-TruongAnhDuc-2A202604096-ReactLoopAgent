# CP6 · Eval lần 2

**Mục tiêu:** đo kết quả sau cải tiến trên cùng điều kiện với CP4.

**Trạng thái trong repo này:** hoàn thành. Cả hai file có 22/22 case, cùng cấu hình OpenRouter `openai/gpt-4o-mini`, judge cùng model, snapshot core và `max_steps=8`. Tổng điểm baseline là 80.18; sau cải tiến là 80.23. H6 tăng từ 55 lên 60.

## Các bước

1. Giữ nguyên agent model, judge model, snapshot, dataset và `max_steps` so với `eval_before.json`.
2. Chạy:

   ```powershell
   python evals/run_evals.py --output eval_after.json
   ```

3. Xác nhận đủ 22 case và điểm tổng khác `null`.
4. So sánh điểm tổng và điểm case đã chọn; đọc trace trước/sau để xem lỗi đã được sửa, còn lại hay phát sinh lỗi mới.
5. Ghi số model calls, token và chi phí nếu có vào mục 4 của [`NOTES.md`](../NOTES.md).
6. Ghi giới hạn của judge, snapshot cố định và việc chỉ chạy một lần mỗi phiên bản vào mục 5.

## Hoàn thành khi

- Hai file eval có cùng cấu hình và đủ case đã chấm.
- NOTES có so sánh dựa trên dữ liệu thực tế, không sửa tay kết quả.
