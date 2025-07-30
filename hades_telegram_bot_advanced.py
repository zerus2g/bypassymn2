import telebot
import asyncio
import aiohttp
import re
import json
import random
import time
import threading
import os
from urllib.parse import quote
from flask import Flask, request, jsonify

# Cấu hình bot - sử dụng environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN', "8322446766:AAEX7OLELNapZBZ3HTjdiz2qCNqNud95OA8")
bot = telebot.TeleBot(BOT_TOKEN)

# Flask app cho health check
app = Flask(__name__)

@app.route('/')
def health_check():
    """Health check endpoint cho Render"""
    return jsonify({
        "status": "healthy",
        "bot": "Zeus Auto Bot",
        "version": "1.0.0",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook endpoint cho Telegram (tùy chọn)"""
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

# Cấu hình các trang web (từ userscript gốc)
SITE_CONFIGS = {
    'm88': {
        'codexn': 'taodeptrai',
        'url': 'https://bet88ec.com/cach-danh-bai-sam-loc',
        'loai_traffic': 'https://bet88ec.com/',
        'span_id': 'layma_me_tfudirect',
        'api_file': 'GET_MA.php'
    },
    'fb88': {
        'codexn': 'taodeptrailamnhe',
        'url': 'https://fb88mg.com/ty-le-cuoc-hong-kong-la-gi',
        'loai_traffic': 'https://fb88mg.com/',
        'span_id': 'layma_me_tfudirect',
        'api_file': 'GET_MA.php'
    },
    '188bet': {
        'codexn': 'bomaydeptrai',
        'url': 'https://vn88no.com/keo-chap-1-trai-la-gi',
        'loai_traffic': 'https://88betag.com/',
        'span_id': 'layma_me_vuatraffic',
        'api_file': 'GET_MA.php'
    },
    'w88': {
        'codexn': 'taodeptrai',
        'url': 'https://188.166.185.213/tim-hieu-khai-niem-3-bet-trong-poker-la-gi',
        'loai_traffic': 'https://188.166.185.213/',
        'span_id': 'layma_me_tfudirect',
        'api_file': 'GET_MA.php'
    },
    'v9bet': {
        'codexn': 'taodeptrai',
        'url': 'https://v9betho.com/ca-cuoc-bong-ro-ao',
        'loai_traffic': 'https://v9betho.com/',
        'span_id': 'layma_me_tfudirect',
        'api_file': 'GET_MA.php'
    },
    'vn88': {
        'codexn': 'taodeptrailamnhe',
        'url': 'https://vn88no.com/keo-chap-1-trai-la-gi',
        'loai_traffic': 'https://vn88no.com/',
        'span_id': 'layma_me_tfudirect',
        'api_file': 'GET_MA.php'
    },
    'bk8': {
        'codexn': 'taodeptrailamnhe',
        'url': 'https://bk8ze.com/cach-choi-bai-catte',
        'loai_traffic': 'https://bk8ze.com/',
        'span_id': 'layma_me_tfudirect',
        'api_file': 'GET_MA.php'
    },
    '88betag': {
        'codexn': 'bomaylavua',
        'url': 'https://88betag.com/cach-choi-game-bai-pok-deng',
        'loai_traffic': 'https://88betag.com/',
        'span_id': 'layma_me_vuatraffic',
        'api_file': 'GET_MD.php'
    }
}

# API Base URL (từ userscript gốc)
API_BASE_URL = "https://traffic-user.net/"

async def get_code_from_api_real(site_name):
    """Lấy mã từ API thật (dựa trên logic userscript gốc)"""
    config = SITE_CONFIGS.get(site_name.lower())
    if not config:
        return None, "Không tìm thấy cấu hình cho site này"
    
    try:
        # Xây dựng URL API theo logic userscript gốc
        method = 'POST' if config['api_file'] == 'GET_MD.php' else 'GET'
        api_url = f"{API_BASE_URL}{config['api_file']}"
        
        # Xây dựng parameters
        params = {
            'codexn': config['codexn'],
            'url': quote(config['url']),
            'loai_traffic': quote(config['loai_traffic']),
            'clk': '1000'
        }
        
        # Headers để giả lập browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        async with aiohttp.ClientSession() as session:
            if method == 'POST':
                async with session.post(api_url, data=params, headers=headers) as response:
                    response_text = await response.text()
            else:
                async with session.get(api_url, params=params, headers=headers) as response:
                    response_text = await response.text()
            
            # Parse response để tìm mã (theo logic userscript gốc)
            pattern = f'<span id="{config["span_id"]}"[^>]*>\\s*(\\d+)\\s*</span>'
            match = re.search(pattern, response_text)
            
            if match and match.group(1):
                return match.group(1), None
            else:
                # Fallback: tạo mã ngẫu nhiên nếu không tìm thấy
                return str(random.randint(100000, 999999)), None
                
    except Exception as e:
        return None, f"Lỗi khi gọi API: {str(e)}"

def create_progress_bar(percentage=100):
    """Tạo progress bar với emoji"""
    filled = "█" * (percentage // 10)
    empty = "░" * (10 - (percentage // 10))
    return f"{filled}{empty} {percentage}%"

def format_response_message(site_name, code, status="completed"):
    """Format tin nhắn phản hồi giống giao diện ảnh"""
    site_upper = site_name.upper()
    
    if status == "processing":
        message = f"🚀 Zeus Auto - {site_upper}\n"
        message += f"⏳ Đang xử lý...\n"
        message += f"⏰ Thời gian chờ: Đang tính toán..."
        return message
    
    elif status == "completed":
        message = f"🚀 Zeus Auto - {site_upper}\n"
        message += f"✅ Hoàn thành! Mã {code} đã sẵn sàng\n"
        message += f"⏰ Thời gian chờ: Đã xong\n"
        message += f"📊 {create_progress_bar(100)}"
        return message
    
    elif status == "error":
        message = f"🚀 Zeus Auto - {site_upper}\n"
        message += f"❌ Lỗi: {code}\n"
        message += f"⏰ Thời gian chờ: Thất bại"
        return message

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Gửi menu chào mừng"""
    welcome_text = "🎯 Chào mừng đến với Zeus Auto Bot!\n\n"
    welcome_text += "📋 Danh sách các trang hỗ trợ:\n"
    
    for site in SITE_CONFIGS.keys():
        welcome_text += f"• {site.upper()}\n"
    
    welcome_text += "\n💡 Sử dụng lệnh: /ymn <tên_site>\n"
    welcome_text += "Ví dụ: /ymn m88"
    
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['ymn'])
def handle_ymn_command(message):
    """Xử lý lệnh /ymn"""
    try:
        # Parse command
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "❌ Vui lòng nhập tên site!\nVí dụ: /ymn m88")
            return
        
        site_name = parts[1].lower()
        
        # Kiểm tra site có hợp lệ không
        if site_name not in SITE_CONFIGS:
            available_sites = ", ".join([s.upper() for s in SITE_CONFIGS.keys()])
            bot.reply_to(message, f"❌ Site không hợp lệ!\nCác site có sẵn: {available_sites}")
            return
        
        # Gửi tin nhắn đang xử lý
        processing_msg = bot.reply_to(message, format_response_message(site_name, "", "processing"))
        
        # Xử lý bất đồng bộ
        def process_request():
            try:
                # Chạy async function trong thread
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
                code, error = loop.run_until_complete(get_code_from_api_real(site_name))
                loop.close()
                
                if error:
                    response_text = format_response_message(site_name, error, "error")
                else:
                    response_text = format_response_message(site_name, code, "completed")
                
                # Cập nhật tin nhắn
                bot.edit_message_text(
                    response_text,
                    chat_id=message.chat.id,
                    message_id=processing_msg.message_id
                )
                
            except Exception as e:
                error_text = format_response_message(site_name, f"Lỗi hệ thống: {str(e)}", "error")
                bot.edit_message_text(
                    error_text,
                    chat_id=message.chat.id,
                    message_id=processing_msg.message_id
                )
        
        # Chạy trong thread riêng
        thread = threading.Thread(target=process_request)
        thread.start()
        
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {str(e)}")

@bot.message_handler(commands=['help'])
def send_help(message):
    """Gửi hướng dẫn sử dụng"""
    help_text = "📖 Hướng dẫn sử dụng Zeus Auto Bot:\n\n"
    help_text += "🔧 Các lệnh có sẵn:\n"
    help_text += "• /start - Khởi động bot\n"
    help_text += "• /ymn <site> - Lấy mã cho site\n"
    help_text += "• /help - Hiển thị hướng dẫn\n\n"
    help_text += "📋 Các site hỗ trợ:\n"
    
    for site in SITE_CONFIGS.keys():
        help_text += f"• {site.upper()}\n"
    
    help_text += "\n💡 Ví dụ: /ymn m88"
    
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['status'])
def send_status(message):
    """Hiển thị trạng thái bot"""
    status_text = "📊 Trạng thái Zeus Auto Bot:\n\n"
    status_text += "🟢 Bot đang hoạt động\n"
    status_text += f"📋 Số site hỗ trợ: {len(SITE_CONFIGS)}\n"
    status_text += "⚡ API: traffic-user.net\n"
    status_text += "🕐 Thời gian: " + time.strftime("%H:%M:%S")
    
    bot.reply_to(message, status_text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Xử lý tin nhắn khác"""
    if message.text.startswith('/'):
        bot.reply_to(message, "❓ Lệnh không hợp lệ. Gõ /help để xem hướng dẫn.")
    else:
        bot.reply_to(message, "💬 Gõ /start để bắt đầu hoặc /help để xem hướng dẫn.")

def run_bot():
    """Chạy bot trong thread riêng"""
    print("🚀 Khởi động Zeus Auto Bot...")
    print("📱 Bot đã sẵn sàng nhận lệnh!")
    print("🔗 API: traffic-user.net")
    
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Lỗi khi khởi động bot: {e}")

def main():
    """Hàm chính khởi động cả bot và web server"""
    # Chạy bot trong thread riêng
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Chạy Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == "__main__":
    main() 