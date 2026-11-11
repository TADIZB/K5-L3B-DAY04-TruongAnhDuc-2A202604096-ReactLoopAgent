# CP5 · Phân tích và cải tiến

**Mục tiêu:** chọn một lỗi có bằng chứng từ baseline, sửa agent và ghi lại lý do.

**Case được chọn trong repo này:** H6 (55/100). Trace cho thấy agent thấy liên kết tới combined incident `xr3myzj7ms51` nhưng không gọi tool để đọc nó. Agent hiện tự đọc incident được liên kết khi câu hỏi yêu cầu và yêu cầu model đưa toàn bộ URL nguồn vào một câu trả lời. CP6 cho thấy H6 đạt 60/100.

## Các bước

1. Chọn một case điểm thấp hoặc có lỗi nhìn thấy trong trace của `eval_before.json`.
2. Ghi ID case, câu trả lời, điểm và đoạn trace liên quan vào [`NOTES.md`](../NOTES.md).
3. Giải thích nguyên nhân có thể xảy ra: xử lý nguồn/scope, partial failure, prompt injection, nhiều bước, dữ liệu dài, tiền đề sai hoặc tool không cần thiết.
4. Thực hiện một thay đổi nhỏ trong `agent.py` nhắm tới lỗi đã chọn. Ví dụ bài chính yêu cầu kiểm tra URL nguồn khi có incident lấy thành công.
5. Chạy lại tests offline:

   ```powershell
   python -m unittest discover -s tests -v
   ```

6. Không sửa fixtures, case, scenario, grading, rubric hoặc kết quả eval thủ công.

## Hoàn thành khi

- `NOTES.md` có case và bằng chứng trace thật.
- Có thay đổi agent giải quyết lỗi đã chọn.
- Tests đạt và có thể giải thích được code đã nộp.
