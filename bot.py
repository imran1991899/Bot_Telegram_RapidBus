import os
import telebot
import pytz
from datetime import datetime

# Credentials from GitHub Secrets
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TOKEN)

# Ensure these match your uppercase .MP4 extension in GitHub
POSTER_A = "posters/poster_a.MP4"
POSTER_B = "posters/poster_b.MP4"

def main():
    try:
        # Set to Malaysia Time
        tz = pytz.timezone('Asia/Kuala Lumpur')
        now = datetime.now(tz)
        hour = now.hour

        # Log for GitHub (this won't show in Telegram)
        print(f"Bot woke up. Malaysia Hour: {hour}")

        # Post A at 5:00 AM or 12:00 PM
        if hour == 5 or hour == 12:
            with open(POSTER_A, 'rb') as video:
                bot.send_video(CHAT_ID, video)
            print("Successfully sent Poster A")
        
        # Post B at 9:00 AM
        elif hour == 9:
            with open(POSTER_B, 'rb') as video:
                bot.send_video(CHAT_ID, video)
            print("Successfully sent Poster B")
        
        else:
            print("Not a scheduled hour. Closing.")

    except Exception as e:
        # If there's an error (like file not found), it shows in GitHub Logs
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
