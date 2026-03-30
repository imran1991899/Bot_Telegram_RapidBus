import os
import telebot
import sys  # Added to read the POSTER_A / POSTER_B argument

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = telebot.TeleBot(TOKEN)

def find_specific_video(target_name):
    """
    Looks for a video file that contains the target_name (e.g., 'POSTER_A')
    """
    target_name = target_name.lower()
    for root, dirs, files in os.walk("."):
        for file in files:
            # Check if it's an MP4 AND if the filename matches our target
            if file.lower().endswith(".mp4") and target_name in file.lower():
                return os.path.join(root, file)
    return None

def main():
    print("--- DEBUG START ---")
    
    # 1. Get the target from GitHub command (e.g., POSTER_A)
    # If no argument is given, it defaults to searching for any mp4
    target = sys.argv[1] if len(sys.argv) > 1 else ""
    print(f"Searching for: {target}")

    # 2. Find the specific file
    video_path = find_specific_video(target)
    
    if not video_path:
        print(f"ERROR: No MP4 file found containing '{target}'!")
        print(f"Current directory contents: {os.listdir('.')}")
        return

    print(f"Found video at: {video_path}")
    print(f"Target Chat ID: {CHAT_ID}")

    try:
        with open(video_path, 'rb') as video:
            # Using the target name as the caption so you know which is which
            bot.send_video(CHAT_ID, video, caption=f"BOT POST: {target}")
        print(f"SUCCESS: {target} sent to Telegram!")
    except Exception as e:
        print(f"TELEGRAM REJECTED THE POST: {e}")
        raise e

if __name__ == "__main__":
    main()
