from __future__ import print_function

import os.path
from urllib.parse import urlparse
from urllib.parse import parse_qs
import json

import googleapiclient
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def get_links_from_spreadsheet(id: str, token_file_name: str):
    creds = None
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_file_name, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id, range='Songs!A:A').execute()
        values = result.get('values')

        if not values:
            return 'No data.'
        else:
            return [v[0] for v in values]

    except HttpError as err:
        print(err)


def get_links_from_playlist(link: str, developer_key: str) -> list:
    parsed_url = urlparse(link)
    playlist_id = parse_qs(parsed_url.query)['list'][0]

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=25,
        playlistId=playlist_id
    )
    response = request.execute()

    returnlinks = []

    for r in response['items']:
        returnlinks.append(f"https://youtube.com/watch?v={r['snippet']['resourceId']['videoId']}")

    return returnlinks


if __name__ == '__main__':
    print(get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json'))

    with open('apikey') as f:
        apikey = list(f)[0].strip()

    print(get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK', apikey))
