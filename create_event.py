import os.path #Module for working with file paths
from google.auth.transport.requests import Request #Module for handling authentication requests
from google.oauth2.credentials import Credentials #module for managing OAuth 2 0 credentials
from google_auth_oauthlib.flow import InstalledAppFlow #Module for handling OAuth 2.0 authentication flow
from googleapiclient.discovery import build #Module for building API service objects
from googleapiclient.errors import HttpError  #Module for handling Google API HTTP errors

# Define the access scope for the google calendar API

SCOPES = ["https://www.googleapis.com/auth/calendar"]

#function to get Google Calendar API credentials
def get_credentials():
    creds = None #initialize as none
    #check if the credentials file exists in credentials folder
    if os.path.exists(r"CREDENTIALS\token.json"):
        #load credentials from file if it exists
        creds = Credentials.from_authorized_user_file(r"CREDENTIALS\token.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(r"CREDENTIALS\credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open(r"CREDENTIALS\token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def create_event(service,startDate,endDate):
    try: 
        event = {
            "summary": "Urban Air", 
            "colorId": 2, 
            'start': {
                'dateTime': startDate, #military time -05:00 is new york time zone
                'timeZone': 'America/New_York'
            }, 
             'end': {
                 'dateTime': endDate, #military time -05:00 is new york time zone
                 'timeZone': 'America/New_York'
             },
             "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"], 
            }

        created_event = service.events().insert(calendarId="primary", body=event).execute()

        print(f"Event created: {created_event.get('htmlLink')}")

    except HttpError as error:
        print(f"An error occurred: {error}")

def main():
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)
    create_event(service,"2024-03-04T16:00:00-05:00","2024-03-04T20:00:00-05:00")

if __name__ == "__main__":
    main()
