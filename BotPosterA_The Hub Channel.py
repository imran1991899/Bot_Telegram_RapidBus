import os
import telebot

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TOKEN)

def find_video_file():
    # This looks through every folder in your repo for a video
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower().endswith(".mp4"):
                return os.path.join(root, file)
    return None

def main():
    print("--- DEBUG START ---")
    
    video_path = find_video_file()
    
    if not video_path:
        print("ERROR: No MP4 file found anywhere in the repository!")
        # List files to help you debug
        print(f"Current directory contents: {os.listdir('.')}")
        return

    print(f"Found video at: {video_path}")
    print(f"Target Chat ID: {CHAT_ID}")

    try:
        with open(video_path, 'rb') as video:
            bot.send_video(CHAT_ID, video, caption="Testing RapidBus Bot")
        print("SUCCESS: Video sent to Telegram!")
    except Exception as e:
        print(f"TELEGRAM REJECTED THE POST: {e}")
        raise e

if __name__ == "__main__":
    main()
