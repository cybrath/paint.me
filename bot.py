import os
import tweepy
from dotenv import load_dotenv
from image_generator import generate_abstract_image
from utils import upload_image

# Load environment variables
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define the bot class
class PaintMeBot(tweepy.StreamListener):
    def on_status(self, status):
        try:
            if "paint me @paintdotme" in status.text.lower():
                user_handle = status.user.screen_name
                print(f"Generating painting for @{user_handle}...")

                # Generate abstract painting
                image_path = generate_abstract_image(user_handle)

                # Upload the painting and reply to the user
                media_id = upload_image(api, image_path)
                reply_text = f"@{user_handle} painted 🎨"
                api.update_status(status=reply_text, in_reply_to_status_id=status.id, media_ids=[media_id])

                print(f"Painting sent to @{user_handle}!")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting Paint.Me bot...")
    listener = PaintMeBot()
    stream = tweepy.Stream(auth=api.auth, listener=listener)
    stream.filter(track=["@paintdotme"], is_async=True)
