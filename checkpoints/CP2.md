# CP2 · Agent loop

**Mục tiêu:** hoàn thiện `run_agent(question, provider, tools, max_steps=6)` trong [`agent.py`](../agent.py).

## Các bước

1. Tạo lịch sử hội thoại gồm system prompt và câu hỏi người dùng.
2. Gọi `provider.complete(messages, schemas)`; một lần gọi model là một step.
3. Thêm nguyên assistant message vào lịch sử trước khi thêm kết quả tool.
4. Parse arguments rồi gọi `tools.execute(name, args)` cho tất cả tool calls trong phản hồi.
5. Gửi từng kết quả lại dưới dạng tool message, gắn đúng `tool_call_id`.
6. Lặp lại đến khi model trả lời cuối hoặc hết `max_steps`.
7. Ghi trace dạng có `event`; tool event cần có `step`, `name`, `arguments` và `result`.

## Hoàn thành khi

- Tool result được trả cho đúng call ID.
- Một phản hồi có nhiều tool calls được xử lý đầy đủ trước lần gọi model tiếp.
- Chỉ kết thúc bình thường khi `finish == 'stop'` và không còn calls.

**Trạng thái trong repo này:** hoàn thành; các test loop trong `tests/test_lab.py` đạt.
