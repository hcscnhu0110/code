import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_secrets_file = "client_secret.json"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials = credentials)

def add(youtube,video_id) :
    request = youtube.playlistItems().insert(
        part = "snippet",
        body = {
            "snippet" : {
                "playlistId" : "PL26dUeKw1pfOeR2jNLJHMYRKL3XPYfGXS",
                "resourceId" : {
                    "kind" : "youtube#video",
                    "videoId" : video_id
                }
            }
        }
    )
    request.execute()

def delete(youtube,keyword) :
    request1 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 25,
        playlistId = "PL26dUeKw1pfOeR2jNLJHMYRKL3XPYfGXS" 
    )
    response = request1.execute()
    find_id = ""
    flag = 0
    for i in range(len(response['items'])) :
        if response['items'][i]['snippet']['resourceId']['videoId'] == keyword or response['items'][i]['snippet']['title'] == keyword :
            find_id += response['items'][i]['id']
            flag = 1
    if flag == 0 :
        print("Sorry,video doesn't exist.")
    else :
        request2 = youtube.playlistItems().delete(
            id = find_id
        )
        request2.execute()

'''def search(youtube,keyword) :'''

def main(youtube):
    try :
        while True :
            print("What do you want to do ?")
            command = input()
            if command == "add" :
                print("Please input the video_id :")
                video_id = input()
                add(youtube,video_id)
            elif command == "delete" :
                print("Please input the keyword :")
                keyword = input()
                delete(youtube,keyword)
    except EOFError :
        pass

main(youtube)
