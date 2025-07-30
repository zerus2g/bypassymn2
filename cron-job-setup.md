# 🚀 Hướng dẫn Setup Cron-Job.com để Bot chạy 24/24

## 📋 Tổng quan

Cron-job.com là dịch vụ miễn phí cho phép chạy các job định kỳ. Chúng ta sẽ sử dụng nó để ping bot liên tục, giữ cho bot không bị sleep trên Render.com.

## 🛠️ Bước 1: Đăng ký Cron-Job.com

1. Truy cập [cron-job.org](https://cron-job.org)
2. Đăng ký tài khoản miễn phí
3. Xác nhận email

## 🚀 Bước 2: Tạo Cron Job

### Cách 1: Sử dụng Web Interface

1. **Đăng nhập vào Cron-Job.com**
2. **Click "Create cronjob"**
3. **Cấu hình như sau:**

```
Title: Zeus Bot Keep Alive
URL: https://your-bot-name.onrender.com/
Schedule: Every 5 minutes
```

4. **Advanced Settings:**
   - **HTTP Method:** GET
   - **Timeout:** 30 seconds
   - **Retry on failure:** Yes
   - **Max retries:** 3

### Cách 2: Sử dụng API (Khuyến nghị)

1. **Tạo API Key:**
   - Vào Settings → API Keys
   - Tạo API key mới

2. **Sử dụng cURL để tạo job:**
```bash
curl -X POST "https://api.cron-job.org/jobs" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "job": {
      "title": "Zeus Bot Keep Alive",
      "url": "https://your-bot-name.onrender.com/",
      "enabled": true,
      "saveResponses": true,
      "schedule": {
        "timezone": "Asia/Ho_Chi_Minh",
        "hours": [-1],
        "mdays": [-1],
        "months": [-1],
        "wdays": [-1],
        "minutes": [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
      }
    }
  }'
```

## ⚙️ Bước 3: Cấu hình nâng cao

### 1. Multiple Ping URLs

Tạo nhiều cron job với các URL khác nhau:

```
Job 1: https://your-bot-name.onrender.com/
Job 2: https://your-bot-name.onrender.com/ping
Job 3: https://your-bot-name.onrender.com/webhook
```

### 2. Custom Headers (Tùy chọn)

```
User-Agent: Cron-Job-Bot/1.0
X-Ping: keep-alive
```

### 3. Notification Settings

1. **Email Notifications:**
   - Bật email notification khi job fail
   - Nhận alert khi bot không phản hồi

2. **Webhook Notifications:**
   - Gửi notification đến Telegram khi có lỗi

## 📊 Bước 4: Monitoring

### 1. Dashboard Monitoring

- Vào Dashboard → Jobs
- Xem status của các job
- Kiểm tra response time
- Xem logs chi tiết

### 2. Response Monitoring

```json
{
  "status": "healthy",
  "bot": "Zeus Auto Bot",
  "version": "1.0.0",
  "timestamp": "2024-01-01 12:00:00"
}
```

### 3. Alert Settings

```
Success Criteria: HTTP 200
Failure Alert: After 2 consecutive failures
Retry: 3 times with 5-minute intervals
```

## 🔧 Bước 5: Tối ưu hóa

### 1. Schedule Optimization

**Khuyến nghị:**
- **Mỗi 5 phút:** Ping chính
- **Mỗi 15 phút:** Ping backup
- **Mỗi giờ:** Deep health check

### 2. Multiple Endpoints

```bash
# Job 1: Health Check
URL: https://your-bot.onrender.com/

# Job 2: Ping Endpoint  
URL: https://your-bot.onrender.com/ping

# Job 3: Custom Ping
URL: https://your-bot.onrender.com/webhook
```

## 🚨 Troubleshooting

### Lỗi thường gặp:

1. **"Job failed - Connection timeout"**
   - Bot đang sleep
   - Kiểm tra URL có đúng không
   - Tăng timeout lên 60 giây

2. **"HTTP 503 - Service unavailable"**
   - Bot đang restart
   - Đợi 2-3 phút rồi thử lại
   - Kiểm tra logs trên Render

3. **"Job not running"**
   - Kiểm tra job có enabled không
   - Kiểm tra schedule có đúng không
   - Test manual execution

### Debug Commands:

```bash
# Test manual ping
curl -X GET "https://your-bot.onrender.com/"

# Test with timeout
curl --max-time 30 "https://your-bot.onrender.com/"

# Test with custom headers
curl -H "User-Agent: Cron-Job-Bot" "https://your-bot.onrender.com/"
```

## 📱 Test Setup

### 1. Manual Test

1. Vào Dashboard → Jobs
2. Click "Execute now" trên job
3. Kiểm tra response

### 2. Automated Test

```bash
# Test script
python keep_alive.py
```

### 3. Monitor Results

```
✅ [12:00:00] Bot is alive - Status: 200
✅ [12:05:00] Bot is alive - Status: 200
✅ [12:10:00] Bot is alive - Status: 200
```

## 💰 Chi phí

- **Free Tier:** 5 jobs, unlimited executions
- **Pro Tier:** $5/month - 50 jobs, advanced features
- **Enterprise:** Custom pricing

## 🔒 Bảo mật

1. **Không expose sensitive data trong URL**
2. **Sử dụng HTTPS cho tất cả endpoints**
3. **Monitor logs để phát hiện abuse**

## 📞 Hỗ trợ

### Cron-Job.com Support:
- Documentation: [docs.cron-job.org](https://docs.cron-job.org)
- Community: [community.cron-job.org](https://community.cron-job.org)
- Email: support@cron-job.org

### Bot Monitoring:
- Render Dashboard: Monitor bot logs
- Cron-Job Dashboard: Monitor ping status
- Telegram Bot: Test bot functionality

## 🎯 Kết quả cuối cùng

Sau khi setup thành công:
- ✅ Bot chạy 24/24 không bị sleep
- ✅ Auto ping mỗi 5 phút
- ✅ Alert khi bot down
- ✅ Monitoring dashboard
- ✅ Backup ping endpoints 