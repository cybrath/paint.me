import os
import logging

def setup_logging():
    """Sets up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("bot.log"),
            logging.StreamHandler()
        ]
    )

setup_logging()

def upload_image(api, image_path):
    """Uploads an image to Twitter and returns the media ID."""
    try:
        logging.info(f"Attempting to upload image: {image_path}")
        media = api.media_upload(image_path)
        logging.info(f"Image uploaded successfully: {image_path}")

        # Clean up the local image file to save disk space
        if os.path.exists(image_path):
            os.remove(image_path)
            logging.info(f"Temporary file removed: {image_path}")

        return media.media_id_string

    except Exception as e:
        logging.error(f"Error uploading image: {e}")
        raise

def format_reply_text(user_handle, custom_message):
    """Formats a reply text with the user handle and a custom message."""
    return f"@{user_handle} {custom_message} "
