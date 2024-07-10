import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from creds import auth_user

def retrieve():

    creds = auth_user()

    try:
        service = build("gmail", "v1", credentials=creds)

        threads = (
            service.users().threads().list(userId="me").execute().get("threads", [])
        )
        
        for thread in threads:
            tdata = (
                service.users().threads().get(userId="me", id=thread["id"]).execute()
            )

        print(tdata)
        


    except HttpError as err:
        print(f"Error! {err}")

retrieve()