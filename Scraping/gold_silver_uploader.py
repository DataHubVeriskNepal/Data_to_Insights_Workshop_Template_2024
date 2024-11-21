import os
import logging
from dotenv import load_dotenv
from utils.s3_uploader import S3Uploader

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(folder='gold_silver', filename='gold_silver.csv'):
    # Load environment variables
    if not load_dotenv():
        logging.warning(".env file not found. Ensure environment variables are set manually.")

    # Initialize S3Uploader
    s3_uploader = S3Uploader()

    # Construct file paths
    filepath = os.path.join(folder, filename)
    s3_file = f'{folder}/{filename}'

    try:
        # Validate file existence
        if not os.path.exists(filepath):
            logging.error(f"File not found: {filepath}")
            return

        # Upload to S3
        logging.info(f"Uploading {filepath} to S3 as {s3_file}...")
        s3_uploader.upload_file(filepath, s3_file)
        logging.info(f"File uploaded successfully to S3: {s3_file}")
    except Exception as e:
        logging.error(f"An error occurred during S3 upload: {e}", exc_info=True)

if __name__ == '__main__':
    main()
