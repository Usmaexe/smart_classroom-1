import os
from google.cloud import storage


bucket_name = 'folderforpicz'
source_folder = 'Images'
credentials_path = 'venv/smart-project-411203-f5188711bb5d.json'

storage_client = storage.Client.from_service_account_json(credentials_path)
bucket = storage_client.bucket(bucket_name)

for filename in os.listdir(source_folder):
    local_path = os.path.join(source_folder, filename)
    blob = bucket.blob(filename)
    blob.upload_from_filename(local_path)
    print(f"File {filename} uploaded to {bucket_name}.")