import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from creds import auth_user

def main():
    creds = auth_user()

    try:
        service = build("gmail", "v1", credentials=creds)
        results = service.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])

        if not labels:
            print("No labels")
            return
        print("Labels:")
        for label in labels:
            print(label["name"])

    except HttpError as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    main()