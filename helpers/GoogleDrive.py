import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# authenticate the google drive api
def authenticate_google_drive():
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = None
    
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("🔴 INVALID GOOGLE CREDENTIALS")
        return

    # First check if we have valid token stored
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let's create new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(
                {
                    "installed": {
                        "client_id": client_id,
                        "client_secret": client_secret,
                        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "redirect_uris": ["http://localhost:8080"]
                    }
                },
                SCOPES
            )
            creds = flow.run_local_server(port=8080)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)
        # Call the Drive v3 API
        return service
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")

# get the root images folder from the google drive
def get_images_folder(service):
    try:
        # first, find the root "images" folder inside of the drive
        all_images = service.files().list(
            q="name='images' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            spaces="drive",
            fields="files(id, name)"
        ).execute()

        # if the folder doesn't exist, create it
        if not all_images.get("files"):
            folder = service.files().create(
                body={"name": "images", "mimeType": "application/vnd.google-apps.folder"},
                fields="id"
            ).execute()
            return folder.get('id')
            
        return all_images['files'][0]['id']
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
    
# Create the subfolder for the generated images to be saved
def create_subfolder(service, images_folder_id, subfolder_name):
    try:
        # create the metadata for the subfolder
        file_metadata = {
            "name": subfolder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [images_folder_id]
        }

        # create the subfolder
        subfolder = service.files().create(body=file_metadata, fields="id").execute()

        # return the subfolder id to use it later
        return subfolder.get('id')
    
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

__all__ = ["authenticate_google_drive", "get_images_folder", "create_subfolder"]

    
    

