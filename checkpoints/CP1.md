# CP1 · Setup và khám phá tools

**Mục tiêu:** xác nhận môi trường chạy được, hiểu dữ liệu snapshot và giới hạn của hai tool.

## Các bước

1. Dùng Python 3.10 trở lên trong thư mục repo:

   ```powershell
   python --version
   ```

2. Chạy thử status GitHub và chi tiết incident Cloudflare theo hai lệnh trong phần “Khám phá tools” của [`GUIDE.md`](../GUIDE.md). Chúng không cần LLM API key.
3. Quan sát `overall`, `components`, `incidents`, `updates`, `captured_at` và `url`.
4. Ghi nhớ giới hạn: tìm kiếm component là khớp chuỗi trong tối đa 50 incident; kết quả rỗng không chứng minh không có sự cố. Incident lịch sử và status tổng thể là hai thông tin khác nhau.
5. Cấu hình một provider, model hỗ trợ tool calling và API key trong môi trường hoặc `.env`. Chương trình không tự đọc `.env`; không commit file này và không chia sẻ key.

## Hoàn thành khi

- Python chạy được.
- Hai tool snapshot trả JSON.
- Provider, model và biến key tương ứng đã được cấu hình an toàn.

**Trạng thái trong repo này:** hoàn thành; đã kiểm tra Python 3.12 và hai tool snapshot.
