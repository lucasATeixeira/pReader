from __future__ import print_function
from os import environ, path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def auth():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './sample/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def main(values):
    if not values:
        return print('Sheets robot: Please insert data')

    print('=> Sheets Robot: in progress...')

    try:
        creds = auth()

        service = build('sheets', 'v4', cache_discovery=False, credentials=creds)

        sheet = service.spreadsheets()

        sheet.values().append(
            spreadsheetId=environ.get('SPREADSHEET_ID'),
            range='Faturas!A1',
            valueInputOption='USER_ENTERED',
            body={
                'values': values
            }
            ).execute()

        print('     * Sheets Robot: Done\n')
    except:
        print('Sheets robot: Something went wrong')
