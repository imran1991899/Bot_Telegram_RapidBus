import os
import telebot

# Credentials from GitHub Secrets
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TOKEN)

# Path to your video
VIDEO_PATH = "posters/poster_a.MP4"

def main():
    print("--- STARTING INSTANT TEST ---")
    print(f"Target Chat ID: {CHAT_ID}")
    
    try:
        with open(VIDEO_PATH, 'rb') as video:
            bot.send_video(CHAT_ID, video)
        print("SUCCESS: Video sent to Telegram!")
    except Exception as e:
        print(f"FAILED: {e}")
        print("Check if the Bot is an Admin and if the Chat ID is correct.")

if __name__ == "__main__":
    main()
