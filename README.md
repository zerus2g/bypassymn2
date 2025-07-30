# 🚀 Hades Auto Telegram Bot

Bot Telegram tự động hóa việc lấy mã từ các trang web, được phát triển dựa trên logic từ userscript "BypassYeumoney".

## ✨ Tính năng

- 🤖 Bot Telegram với giao diện đẹp mắt
- 📋 Hỗ trợ nhiều trang web khác nhau
- ⚡ Xử lý bất đồng bộ nhanh chóng
- 🎯 Progress bar và emoji trực quan
- 🔄 Tự động cập nhật trạng thái

## 📋 Các trang web hỗ trợ

- **M88** - Bet88ec
- **FB88** - FB88MG
- **188BET** - 188Bet
- **W88** - W88
- **V9BET** - V9Betho
- **VN88** - VN88
- **BK8** - BK8
- **88BETAG** - 88Betag

## 🛠️ Cài đặt

### 1. Cài đặt Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Tạo Bot Telegram

1. Mở Telegram và tìm `@BotFather`
2. Gửi lệnh `/newbot`
3. Đặt tên cho bot
4. Đặt username cho bot
5. Lưu lại **BOT_TOKEN** được cung cấp

### 3. Cấu hình Bot

1. Mở file `hades_telegram_bot.py`
2. Thay thế `YOUR_BOT_TOKEN_HERE` bằng token thật của bạn:

```python
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"  # Token thật của bạn
```

### 4. Chạy Bot

```bash
python hades_telegram_bot.py
```

## 📱 Cách sử dụng

### Các lệnh có sẵn:

- `/start` - Khởi động bot và xem danh sách trang web
- `/ymn <site>` - Lấy mã cho trang web cụ thể
- `/help` - Xem hướng dẫn sử dụng

### Ví dụ sử dụng:

```
/ymn m88
```

Bot sẽ trả về:
```
🚀 Hades Auto - M88
✅ Hoàn thành! Mã 817363 đã sẵn sàng
⏰ Thời gian chờ: Đã xong
📊 ██████████ 100%
```

## 🔧 Cấu hình nâng cao

### Thêm trang web mới:

Chỉnh sửa `SITE_CONFIGS` trong file `hades_telegram_bot.py`:

```python
'new_site': {
    'codexn': 'your_codexn',
    'url': 'https://example.com/',
    'loai_traffic': 'https://example.com/',
    'span_id': 'your_span_id',
    'api_file': 'GET_MA.php'
}
```

### Tùy chỉnh API:

Chỉnh sửa hàm `get_code_from_api()` để kết nối với API thật thay vì mô phỏng.

## 🚨 Lưu ý quan trọng

- ⚠️ Bot này chỉ là mô phỏng, cần tích hợp API thật để hoạt động
- 🔒 Đảm bảo bảo mật token bot
- 📝 Tuân thủ điều khoản sử dụng của Telegram
- 🛡️ Sử dụng có trách nhiệm và hợp pháp

## 🐛 Xử lý lỗi

### Lỗi thường gặp:

1. **"Bot token không hợp lệ"**
   - Kiểm tra lại token trong file config
   - Đảm bảo bot chưa bị khóa

2. **"Module không tìm thấy"**
   - Chạy `pip install -r requirements.txt`
   - Kiểm tra Python version (yêu cầu 3.7+)

3. **"Lỗi kết nối"**
   - Kiểm tra kết nối internet
   - Thử restart bot

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy:
1. Kiểm tra logs trong console
2. Đảm bảo đã cài đặt đúng dependencies
3. Kiểm tra token bot có hợp lệ không

## 📄 License

Dự án này được phát triển cho mục đích học tập và nghiên cứu. 