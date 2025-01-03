import os
import boto3
import urllib3
from botocore.exceptions import NoCredentialsError, ClientError


# Suppress only the single warning from urllib3 needed.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# session = boto3.Session(profile_name='default')

aws_access_key = os.getenv('AWS_ACCESS')
aws_secret_access_key = os.getenv('AWS_SECRET')
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key
)

s3 = session.client('s3',verify=False)

def list_folders_in_bucket(bucket_name):
    """
    Lists the folders in the specified S3 bucket.
    Args:
        bucket_name: Name of the S3 bucket.
    Returns:
        List of folder names in the S3 bucket.
    """
    try:
        # List objects in the bucket with delimiter '/'
        response = s3.list_objects_v2(Bucket=bucket_name, Delimiter='/')
        folders = [prefix['Prefix'] for prefix in response['CommonPrefixes']]
        return folders
    except NoCredentialsError:
        print("Error: AWS credentials not available.")
        return []
    except ClientError as e:
        print(f"Error: {e}")
        return []

def download_files_from_s3(bucket_name, s3_folder, local_folder):
    """
    Downloads files from the specified S3 folder to the local folder.
    Args:
        bucket_name: Name of the S3 bucket.
        s3_folder: Path to the S3 folder containing the files to download.
        local_folder: Path to the local folder where the files will be downloaded
    """
    
    try:
        # Create local folder if it doesn't exist
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)
        
        # List objects in the specified S3 folder
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder)
        
        # Check if the folder contains files
        if 'Contents' in response:
            for obj in response['Contents']:
                # Get the file name from S3 key
                file_key = obj['Key']
                file_name = os.path.basename(file_key)
                
                if file_name:  # Ensure it's a file, not the folder itself
                    local_file_path = os.path.join(local_folder, file_name)
                    print(f"Downloading {file_key} to {local_file_path} ...")
                    
                    # Download the file
                    s3.download_file(bucket_name, file_key, local_file_path)
        
        else:
            print(f"No files found in {s3_folder}.")
    
    except NoCredentialsError:
        print("Error: AWS credentials not available.")
    except ClientError as e:
        print(f"Error: {e}")


def download_initializer(bucket_name,data_folder):
    """
    Downloads files from the specified S3 bucket to the local folder.
    Args:
        bucket_name: Name of the S3 bucket.
        data_folder: Path to the local folder where the files will be downloaded.
    """

    print("Downloading files from S3 bucket")
    print(f"Bucket Name: {bucket_name}")
    print(f"Data Folder: {data_folder}")
    current_dir = os.getcwd()
    print(data_folder)
    data_folder = os.path.join(current_dir, data_folder)
    print(bucket_name)
    try:
        # List folders in the specified S3 bucket
        s3_folders = list_folders_in_bucket(bucket_name) #["forex", "gold_silver"]
        if s3_folders:
            for s3_folder in s3_folders:
                local_folder = os.path.join(".",data_folder, s3_folder)
                download_files_from_s3(bucket_name, s3_folder, local_folder)
        return True

    except NoCredentialsError:
        print("Error: AWS credentials not available.")
        return False
    except ClientError as e:
        print(f"Error: {e}")
        return False


