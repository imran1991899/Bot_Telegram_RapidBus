import os
import telebot

# Get credentials from GitHub Secrets
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Path to your video - Ensure the filename matches exactly!
# Double check if it is posters/ or poster/
VIDEO_PATH = "poster/poster_a.MP4"

def main():
    print("--- DEBUG START ---")
    print(f"Target Chat ID: {CHAT_ID}")
    
    # 1. Check if the file actually exists in GitHub
    if not os.path.exists(VIDEO_PATH):
        print(f"ERROR: File '{VIDEO_PATH}' not found! Check your folder name.")
        return

    # 2. Attempt to send
    try:
        with open(VIDEO_PATH, 'rb') as video:
            bot.send_video(CHAT_ID, video, caption="Testing RapidBus Bot")
        print("SUCCESS: Video sent to Telegram!")
    except Exception as e:
        # This will print the EXACT reason Telegram rejected it
        print(f"TELEGRAM REJECTED THE POST: {e}")
        # This raises the error so GitHub turns RED
        raise e

if __name__ == "__main__":
    main()
