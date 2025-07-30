import requests
import time
import os
from datetime import datetime

def ping_bot():
    """Ping bot để keep alive"""
    # URL của bot trên Render (thay bằng URL thật của bạn)
    bot_url = os.getenv('BOT_URL', 'https://zeus-auto-bot.onrender.com')
    
    try:
        # Ping health check endpoint
        response = requests.get(f"{bot_url}/", timeout=10)
        
        if response.status_code == 200:
            print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Bot is alive - Status: {response.status_code}")
            return True
        else:
            print(f"❌ [{datetime.now().strftime('%H:%M:%S')}] Bot error - Status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ [{datetime.now().strftime('%H:%M:%S')}] Ping failed: {str(e)}")
        return False

def main():
    """Main function để ping bot"""
    print("🔄 Starting keep alive script...")
    print(f"🎯 Target URL: {os.getenv('BOT_URL', 'https://zeus-auto-bot.onrender.com')}")
    
    success = ping_bot()
    
    if success:
        print("✅ Keep alive successful!")
        exit(0)
    else:
        print("❌ Keep alive failed!")
        exit(1)

if __name__ == "__main__":
    main() 