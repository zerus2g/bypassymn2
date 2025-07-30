# 🚀 Hướng dẫn Deploy Bot Telegram lên Render.com

## 📋 Yêu cầu trước khi deploy

### 1. Chuẩn bị Bot Telegram
1. Mở Telegram và tìm `@BotFather`
2. Gửi lệnh `/newbot`
3. Đặt tên cho bot (ví dụ: "Zeus Auto Bot")
4. Đặt username cho bot (ví dụ: `zeus_auto_bot`)
5. **Lưu lại BOT_TOKEN** được cung cấp

### 2. Chuẩn bị GitHub Repository
1. Tạo repository mới trên GitHub
2. Upload tất cả file dự án lên repository
3. Đảm bảo repository là public

## 🛠️ Bước 1: Tạo tài khoản Render.com

1. Truy cập [render.com](https://render.com)
2. Đăng ký tài khoản mới hoặc đăng nhập
3. Kết nối với GitHub account

## 🚀 Bước 2: Deploy trên Render.com

### Cách 1: Sử dụng render.yaml (Khuyến nghị)

1. **Tạo Web Service:**
   - Vào Dashboard Render
   - Click "New +" → "Web Service"
   - Connect GitHub repository
   - Chọn repository chứa code bot

2. **Cấu hình Service:**
   - **Name:** `zeus-auto-bot`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python hades_telegram_bot_advanced.py`

3. **Thêm Environment Variables:**
   - Click "Environment" tab
   - Thêm variable:
     - **Key:** `BOT_TOKEN`
     - **Value:** `[BOT_TOKEN_TỪ_BOTFATHER]`

4. **Deploy:**
   - Click "Create Web Service"
   - Đợi build và deploy hoàn tất

### Cách 2: Deploy thủ công

1. **Tạo Web Service:**
   ```
   Name: zeus-auto-bot
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python hades_telegram_bot_advanced.py
   ```

2. **Environment Variables:**
   ```
   BOT_TOKEN = [BOT_TOKEN_TỪ_BOTFATHER]
   ```

## 🔧 Bước 3: Cấu hình Bot

### 1. Kiểm tra Bot hoạt động
- Vào URL được cung cấp bởi Render (ví dụ: `https://zeus-auto-bot.onrender.com`)
- Nếu thấy JSON response là bot đã hoạt động

### 2. Test Bot trên Telegram
- Tìm bot theo username đã tạo
- Gửi lệnh `/start`
- Test lệnh `/ymn m88`

## 📊 Bước 4: Monitoring và Logs

### Xem Logs:
1. Vào Dashboard Render
2. Chọn service `zeus-auto-bot`
3. Click tab "Logs"
4. Kiểm tra logs để debug nếu cần

### Health Check:
- Truy cập: `https://your-app-name.onrender.com/`
- Sẽ thấy JSON response:
```json
{
  "status": "healthy",
  "bot": "Zeus Auto Bot",
  "version": "1.0.0",
  "timestamp": "2024-01-01 12:00:00"
}
```

## 🔄 Bước 5: Auto Deploy

### Cấu hình Auto Deploy:
1. Vào service settings
2. Bật "Auto-Deploy"
3. Mỗi khi push code lên GitHub, Render sẽ tự động deploy

## 🚨 Troubleshooting

### Lỗi thường gặp:

1. **"Bot token không hợp lệ"**
   - Kiểm tra BOT_TOKEN trong Environment Variables
   - Đảm bảo token đúng và bot chưa bị khóa

2. **"Build failed"**
   - Kiểm tra requirements.txt
   - Đảm bảo Python version đúng (3.9.16)

3. **"Service không start"**
   - Kiểm tra logs trong Render dashboard
   - Đảm bảo start command đúng

4. **"Bot không phản hồi"**
   - Kiểm tra bot có đang polling không
   - Test health check endpoint

### Debug Commands:
```bash
# Xem logs real-time
tail -f logs/app.log

# Kiểm tra environment variables
echo $BOT_TOKEN

# Test bot locally
python hades_telegram_bot_advanced.py
```

## 📱 Test Bot

### Các lệnh test:
```
/start - Menu chào mừng
/ymn m88 - Test lấy mã M88
/help - Hướng dẫn sử dụng
/status - Trạng thái bot
```

### Kết quả mong đợi:
```
🚀 Zeus Auto - M88
✅ Hoàn thành! Mã 817363 đã sẵn sàng
⏰ Thời gian chờ: Đã xong
📊 ██████████ 100%
```

## 💰 Chi phí

- **Free Tier:** 750 giờ/tháng
- **Bot sẽ sleep sau 15 phút không hoạt động**
- **Auto wake up khi có request**

## 🔒 Bảo mật

1. **Không commit BOT_TOKEN vào code**
2. **Sử dụng Environment Variables**
3. **Đảm bảo repository không chứa sensitive data**

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra logs trong Render dashboard
2. Test health check endpoint
3. Kiểm tra bot token có hợp lệ không
4. Đảm bảo tất cả dependencies đã được cài đặt

## 🎯 Kết quả cuối cùng

Sau khi deploy thành công:
- ✅ Bot chạy 24/7 trên Render
- ✅ Auto restart khi có lỗi
- ✅ Health check endpoint
- ✅ Logs monitoring
- ✅ Auto deploy từ GitHub 