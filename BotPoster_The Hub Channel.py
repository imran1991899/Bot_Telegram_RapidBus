import os
import telebot
import sys

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID_THC')
bot = telebot.TeleBot(TOKEN)

# Mapping the mode to the specific file path
POSTER_MAP = {
    "POSTER_A": "poster/poster_a.MP4",
    "POSTER_B": "poster/poster_b.MP4" # Ensure you have a poster_b.MP4 in your folder!
}

def main():
    # Get the poster type from the command line argument
    mode = sys.argv[1] if len(sys.argv) > 1 else "POSTER_A"
    video_path = POSTER_MAP.get(mode)

    print(f"--- DEBUG START ---")
    print(f"Mode: {mode}")
    print(f"Target Path: {video_path}")

    if not video_path or not os.path.exists(video_path):
        print(f"ERROR: File '{video_path}' not found!")
        return

    try:
        with open(video_path, 'rb') as video:
            caption = "RapidBus Morning Update" if mode == "POSTER_A" else "RapidBus Midday Update"
            bot.send_video(CHAT_ID, video, caption=caption)
        print(f"SUCCESS: {mode} sent to Telegram!")
    except Exception as e:
        print(f"TELEGRAM REJECTED THE POST: {e}")
        raise e

if __name__ == "__main__":
    main()
