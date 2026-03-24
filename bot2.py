import os
import telebot

# Get credentials from GitHub Secrets
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Path to your video - Ensure the filename matches exactly!
VIDEO_PATH = "posters/poster_a.MP4"

def main():
    print("--- DEBUG INFO ---")
    print(f"Checking for file: {VIDEO_PATH}")
    
    # Check if file exists in the folder
    if not os.path.exists(VIDEO_PATH):
        print(f"ERROR: File '{VIDEO_PATH}' not found in the posters folder!")
        return

    print(f"Attempting to send to Chat ID: {CHAT_ID}")
    
    # We removed 'try/except' so that if it fails, GitHub shows the Red X and the reason
    with open(VIDEO_PATH, 'rb') as video:
        bot.send_video(CHAT_ID, video, caption="Manual Test: Poster A")
    
    print("SUCCESS: Video sent to Telegram!")

if __name__ == "__main__":
    main()
