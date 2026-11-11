# CP3 · Xử lý lỗi và trace

**Mục tiêu:** agent dừng có kiểm soát và để lại trace đủ để kiểm tra.

## Các bước

1. Giới hạn số lần gọi model bằng `max_steps`; hết lượt trả `status: max_steps`.
2. Nếu tool arguments sai JSON, gửi tool result có `error: INVALID_ARGUMENTS` thay vì crash.
3. Ghi lỗi tool/timeout thành observation để model có thể báo thiếu dữ liệu.
4. Lỗi provider và output bị cắt (`finish == 'length'`) phải trả `status: error`, không báo hoàn thành.
5. Lưu finish, usage, các tool calls và kết quả trong trace; không ghi API key hay yêu cầu chain-of-thought.
6. Chạy các test offline:

   ```powershell
   python -m unittest discover -s tests -p test_lab.py -v
   python -m unittest discover -s tests -p test_validation.py -v
   ```

7. Bài chính yêu cầu kiểm tra URL nguồn sau khi lấy incident thành công. Nếu câu trả lời cuối thiếu URL, ghi `validation_missing_source` và yêu cầu model sửa trong số bước còn lại.

## Hoàn thành khi

- Các test loop và validation đạt.
- Lỗi tool không bị biến thành khẳng định trạng thái dịch vụ; provider error không bị báo completed.

**Trạng thái trong repo này:** hoàn thành; 12 test `test_lab.py` và 5 test `test_validation.py` đạt.
