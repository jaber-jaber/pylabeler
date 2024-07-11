import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from creds import auth_user

MY_LABEL = "INBOX"

def retrieve():

    creds = auth_user()

    try:
        service = build("gmail", "v1", credentials=creds)

        # Get Label
        lb_response = service.users().labels().list(userId="me").execute()
        labels = lb_response.get("labels")
        names = [label["id"] for label in labels]
        counter = 0

        try:
            response = service.users().threads().list(userId='me', maxResults=150, labelIds=[MY_LABEL]).execute()
            threads = response.get('threads', [])
            
            for thread in threads:
                thread_id = thread['id']
                thread_details = service.users().threads().get(userId='me', id=thread_id).execute()
                messages = thread_details.get('messages', [])

                for message in messages:
                    headers = message.get('payload', {}).get('headers', [])
                    to_emails = next((header['value'] for header in headers if header['name'] == 'To'), 'No recipients')
                    cc_emails = next((header['value'] for header in headers if header['name'] == 'Cc'), 'No copied')
                        
        except HttpError as emailErr:
            print(f'Error retrieving messages from label: {emailErr}')

    except HttpError as err:
        print(f"Error! {err}")

retrieve()