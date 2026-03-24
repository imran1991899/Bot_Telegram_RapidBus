import os
import telebot
import pytz
from datetime import datetime

# Credentials from GitHub Secrets
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TOKEN)

# Update file names to match your MP4 files
POSTER_A = "posters/poster_a.MP4"
POSTER_B = "posters/poster_b.MP4"

def main():
    try:
        # Malaysia Timezone
        tz = pytz.timezone('Asia/Kuala Lumpur')
        now = datetime.now(tz)
        hour = now.hour

        # Post at 5:00 AM or 12:00 PM
        if hour == 5 or hour == 12:
            with open(POSTER_A, 'rb') as video:
                bot.send_video(CHAT_ID, video)
        
        # Post at 9:00 AM
        elif hour == 9:
            with open(POSTER_B, 'rb') as video:
                bot.send_video(CHAT_ID, video)
                
    except Exception:
        # Stay silent if there is an error
        pass

if __name__ == "__main__":
    main()
