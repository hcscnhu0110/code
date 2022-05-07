import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_secrets_file = "client_secret.json"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)

api_service_name = "youtube"
api_version = "v3"
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials = credentials)


request = youtube.playlistItems().list(
    part = "snippet",
    maxResults = 25,
    playlistId = "PL26dUeKw1pfOeR2jNLJHMYRKL3XPYfGXS",
)
response = request.execute()
print(response['items'])
'''['snippet']['resourceId']['videoId']'''

