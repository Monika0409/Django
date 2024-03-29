from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the service account credentials JSON file
credentials_file = 'weighty-gasket-414010-2cb2a336174b.json'

# Create credentials object from the JSON file
credentials = service_account.Credentials.from_service_account_file(
    credentials_file,
    scopes=['https://www.googleapis.com/auth/drive.metadata.readonly']  # Specify the necessary scope
)

# Build the Drive service
drive_service = build('drive', 'v3', credentials=credentials)

# List all files in the Drive
results = drive_service.files().list().execute()
files = results.get('files', [])

if not files:
    print('No files found.')
else:
    print('Files:')
    for file in files:
        print(f"{file['name']} ({file['id']})")
        