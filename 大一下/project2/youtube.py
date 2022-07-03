import os
import re
import pickle
from time import sleep
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

credentials = None

def create_forever_credentials(credentials) :
    if os.path.exists("token.pickle") :
        with open("token.pickle","rb") as token :
            credentials = pickle.load(token)

    if not credentials or not credentials.valid :
        if credentials and credentials.expired and credentials.refresh_token :
            credentials.refresh(Request())
        else :
            scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
            client_secrets_file = "client_secret.json"
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
            flow.run_local_server(port = 8080,prompt = "consent",authorization_prompt_message = "")
            credentials = flow.credentials
            with open("token.pickle","wb") as f :
                pickle.dump(credentials,f)
    return credentials

def create_youtube(credentials) :
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, credentials = credentials)
    return youtube

def find_playlistId(youtube,playlist_name,channel_id) :
    request = youtube.playlists().list(
        part = "snippet",
        channelId = channel_id,
        maxResults = 25
    )
    response = request.execute()
    flag = 0
    playlist_id = ""
    for i in range(len(response["items"])) :
        if response["items"][i]["snippet"]["title"] == playlist_name :
            playlist_id += response["items"][i]["id"]
            flag = 1
    if flag == 0:
        return 0
    else :
        return playlist_id

def find_videoId(youtube,playlist_id,target) :
    url = re.search('v=\S{11}',target)
    video_id = ""
    if url :
        video_id += url.group()[2:]
    else :
        request = youtube.playlistItems().list(
            part = "snippet",
            maxResults = 50,
            playlistId = playlist_id
        )
        response = request.execute()
        for i in range(len(response['items'])) :
            if response['items'][i]['snippet']['title'] == target :
                video_id += response['items'][i]['snippet']['resourceId']['videoId']
    return video_id
      
def add_video(youtube,channel_id) :
    request1 = youtube.playlists().list(
        part = "snippet",
        channelId = channel_id,
        maxResults = 50
    )
    response1 = request1.execute()
    table = {i + 1 : response1['items'][i]['snippet']['title'] for i in range(len(response1['items']))}
    print("-" * 50)
    print(f"Playlists in Channel")
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table :
        print(key , "\t" , ":" , table[key])
    print("-" * 50)

    Number = int(input("Which PlayList ? (Please input the PlayList Number) :" + "\n"))
    playlist_id = find_playlistId(youtube,table[Number],channel_id)

    num = int(input("Add how many videos ?" + "\n"))
    target = list()
    print("Please input Video URL :")
    for i in range(num) :
        target.append(input())
    for i in range(num) :
        url = re.search('v=\S{11}',target[i])
        video_id = url.group()[2:]
        request2 = youtube.playlistItems().insert(
            part = "snippet",
            body = {
                "snippet" : {
                    "playlistId" : playlist_id,
                    "resourceId" : {
                        "kind" : "youtube#video",
                        "videoId" : video_id
                    }
                }
            }
        )
        request2.execute()
    print("Succeeded!")
    print("-" * 50)

def delete_video(youtube,channel_id) :
    request1 = youtube.playlists().list(
        part = "snippet",
        channelId = channel_id,
        maxResults = 50
    )
    response1 = request1.execute()
    table1 = {i + 1 : response1['items'][i]['snippet']['title'] for i in range(len(response1['items']))}
    print("-" * 50)
    print(f"Playlists in Channel")
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table1 :
        print(key , "\t" , ":" , table1[key])
    print("-" * 50)

    Number1 = int(input("Which PlayList ? (Please input the PlayList Number) :" + "\n"))
    playlist_id = find_playlistId(youtube,table1[Number1],channel_id)

    print("-" * 50)
    print(f"Videos in {table1[Number1]}")
    request2 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response2 = request2.execute()
    table2 = {i + 1 : response2['items'][i]['snippet']['title'] for i in range(len(response2['items']))}
    print("-" * 50)
    print("Number" + "\t" + "   " + "Video Name" )
    for key in table2 :
        print(key , "\t" , ":" , table2[key])
    print("-" * 50)

    num = int(input("Delete how many videos ?" + "\n"))
    print("Please input the Video Number :")
    target = list()
    for i in range(num) :
        Number2 = int(input())
        target.append(table2[Number2])
    for i in range(num) :
        video_id = find_videoId(youtube,playlist_id,target[i])
        find_id = ""
        for j in range(len(response2['items'])) :
            if response2['items'][j]['snippet']['resourceId']['videoId'] == video_id :
                find_id += response2['items'][j]['id']
        request3 = youtube.playlistItems().delete(
            id = find_id
        )
        request3.execute()
    print("Succeeded!")
    print("-" * 50)

def search_video(youtube,playlist_id,target) :
    video_id = find_videoId(youtube,playlist_id,target)
    request1 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response1 = request1.execute()
    request2 = youtube.videos().list(
        part = 'statistics',
        id = video_id
    )
    response2 = request2.execute()
    find_id = ""
    flag = 0
    aim = 0
    for i in range(len(response1['items'])) :
        if response1['items'][i]['snippet']['resourceId']['videoId'] == video_id :
            find_id += response1['items'][i]['id']
            aim = i
            flag = 1
    if flag == 0 :
        print("Sorry,video doesn't exist.")
        print("-" * 50)
    else :
        print("-" * 50)
        print('%30s' % "Information")
        print("-" * 50)
        print("Name : " + "\n" , response1['items'][aim]['snippet']['title'] , "\n" , "=" * 50)
        print("Publication Date : " + "\n" , response1['items'][aim]['snippet']['publishedAt'] , "\n" , "=" * 50)
        print("Views : " + "\n" , response2['items'][0]['statistics']['viewCount'] , "\n" , "=" * 50)
        print("Likes : " + "\n" , response2['items'][0]['statistics']['likeCount'] , "\n" , "=" * 50)
        print("Video Owner Channel : " + "\n" , response1['items'][aim]['snippet']['videoOwnerChannelTitle'] , "\n" , "=" * 50)
        print("Position : " + "\n" , int(response1['items'][aim]['snippet']['position'])+1 , "\n" , "=" * 50)
        print("Details : " + "\n" , response1['items'][aim]['snippet']['description'])
        print("-" * 50)

def change_video_sequence(youtube,channel_id) :     
    request1 = youtube.playlists().list(
        part = "snippet",
        channelId = channel_id,
        maxResults = 50,
    )
    response1 = request1.execute()
    table1 = {i + 1 : response1['items'][i]['snippet']['title'] for i in range(len(response1['items']))}
    print("-" * 50)
    print(f"Playlists in Channel")
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table1 :
        print(key , "\t" , ":" , table1[key])
    print("-" * 50)

    Number1 = int(input("Which PlayList ? (Please input the PlayList Number) :" + "\n"))
    playlist_id = find_playlistId(youtube,table1[Number1],channel_id)

    print("-" * 50)
    print(f"Videos in {table1[Number1]}")
    request2 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response2 = request2.execute()
    table2 = {i + 1 : response2['items'][i]['snippet']['title'] for i in range(len(response2['items']))}
    print("-" * 50)
    print("Number" + "\t" + "   " + "Video Name" )
    for key in table2 :
        print(key , "\t" , ":" , table2[key])
    print("-" * 50)

    print("Please input the Video Number :")
    Number2 = int(input())
    target = table2[Number2]
    video_id = find_videoId(youtube,playlist_id,target)
    find_id = ""
    for j in range(len(response2['items'])) :
        if response2['items'][j]['snippet']['resourceId']['videoId'] == video_id :
            find_id += response2['items'][j]['id']
    site = int(input("Where do you want to move ?" + "\n"))
    request3 = youtube.playlistItems().update(
        part = "snippet",
        body = {
            "id" : find_id,
            "snippet" : {
                "playlistId" : playlist_id,
                "position" : str(site-1),
                "resourceId" : {
                    "kind" : "youtube#video",
                    "videoId" : video_id
                }
            }
        }
    )
    request3.execute()
    print("Succeeded!")
    print("-" * 50)

def move_video_to_another_playlist(youtube,channel_id) :
    request1 = youtube.playlists().list(
        part = "snippet",
        channelId = channel_id,
        maxResults = 50
    )
    response1 = request1.execute()
    table1 = {i + 1 : response1['items'][i]['snippet']['title'] for i in range(len(response1['items']))}
    print("-" * 50)
    print(f"Playlists in Channel")
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table1 :
        print(key , "\t" , ":" , table1[key])
    print("-" * 50)

    Number1 = int(input("From which PlayList ? (Please input the PlayList Number) :" + "\n"))
    playlist_id = find_playlistId(youtube,table1[Number1],channel_id)
    Number1 = int(input("To which PlayList ? (Please input the PlayList Number) :" + "\n"))
    new_playlist_id = find_playlistId(youtube,table1[Number1],channel_id)

    print("-" * 50)
    print(f"Videos in {table1[Number1]}")
    request2 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response2 = request2.execute()
    table2 = {i + 1 : response2['items'][i]['snippet']['title'] for i in range(len(response2['items']))}
    print("-" * 50)
    print("Number" + "\t" + "   " + "Video Name" )
    for key in table2 :
        print(key , "\t" , ":" , table2[key])
    print("-" * 50)

    num = int(input("Move how many videos ?" + "\n"))
    print("Please input the Video Number :")
    target = list()
    for i in range(num) :
        Number2 = int(input())
        target.append(table2[Number2])
    for i in range(num) :
        video_id = find_videoId(youtube,playlist_id,target[i])
        request3 = youtube.playlistItems().insert(
            part = "snippet",
            body = {
                "snippet" : {
                    "playlistId" : new_playlist_id,
                    "resourceId" : {
                        "kind" : "youtube#video",
                        "videoId" : video_id
                    }
                }
            }
        )
        request3.execute()

        find_id = ""
        for j in range(len(response2['items'])) :
            if response2['items'][j]['snippet']['resourceId']['videoId'] == video_id :
                find_id += response2['items'][j]['id']
        request4 = youtube.playlistItems().delete(
            id = find_id
        )
        request4.execute()
    print("Succeeded!")
    print("-" * 50)

def create_playlist(youtube,channel_id) :
    name = input("Please name the PlayList :" + "\n")
    privacy = input("Private or Public ?" + "\n")
    request = youtube.playlists().insert(
        part = "snippet,status",
        body = {
            "snippet" : {
                "title" : name,
            },
            "status" : {
                "privacyStatus" : privacy
            }
        }
    )
    request.execute()

def delete_playlist(youtube,channel_id) :
    request1 = youtube.playlists().list(
        part = "snippet",
        maxResults = 50,
        channelId = channel_id,
    )
    response = request1.execute()
    table = {i + 1 : response['items'][i]['snippet']['title'] for i in range(len(response['items']))}
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table :
        print(key , "\t" , ":" , table[key])
    print("-" * 50)
    number = int(input("Please input the PlayList Number :" + "\n"))
    playlist_id = find_playlistId(youtube,table[number],channel_id)
    request2 = youtube.playlists().delete(
        id = playlist_id
    )
    request2.execute()
    print("Succeeded!")
    print("-" * 50)
    
def playlist_overview(youtube,playlist_name,channel_id) :
    playlist_id = find_playlistId(youtube,playlist_name,channel_id)
    request = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response = request.execute()
    table = {i + 1 : response['items'][i]['snippet']['title'] for i in range(len(response['items']))}
    print("-" * 50)
    print("Number" + "\t" + "   " + "Video Name" )
    for key in table :
        print(key , "\t" , ":" , table[key])
    print("-" * 50)
    print("Video Overview? (Y/N)")
    ask = input()
    while ask == 'Y' :
        Number = int(input("Please input the Video Number (Input 0 to Leave):" + "\n"))
        if Number == 0:
            break
        search_video(youtube,playlist_id,table[Number])

def channel_overview(youtube) :
    url = input("Please input channel URL :" + "\n")
    key = re.search("/channel/\S{24}",url)
    channel_id = key.group()[9:]
    request = youtube.playlists().list(
        part = "snippet",
        channelId = channel_id,
        maxResults = 50
    )
    response = request.execute()
    table = {i + 1 : response['items'][i]['snippet']['title'] for i in range(len(response['items']))}
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table :
        print(key , "\t" , ":" , table[key])
    print("-" * 50)
    print("PlayList Overview? (Y/N)")
    ask = input()
    while ask == 'Y' :
        Number = int(input("Please input the PlayList Number (Input 0 to Leave):" + "\n"))
        if Number == 0 :
            break
        playlist_name = table[Number]
        print(table[Number])
        playlist_overview(youtube,playlist_name,channel_id)

def add_whole_playlist(youtube,playlist_id,my_channel_id) :
    request1 = youtube.playlists().list(
        part = "snippet",
        channelId = my_channel_id,
        maxResults = 50
    )
    response1 = request1.execute()
    table = {i + 1 : response1['items'][i]['snippet']['title'] for i in range(len(response1['items']))}
    print("-" * 50)
    print(f"Playlists in Channel")
    print("-" * 50)
    print("Number" + "\t" + "   " + "PlayList Name" )
    for key in table :
        print(key , "\t" , ":" , table[key])
    print("-" * 50)
    Number = int(input("To which PlayList ? (Please input the PlayList Number) :" + "\n"))
    my_playlist_id = find_playlistId(youtube,table[Number],my_channel_id)
    request2 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response2 = request2.execute()
    for i in range(len(response2['items'])) :
        request2 = youtube.playlistItems().insert(
            part = "snippet",
            body = {
                "snippet" : {
                    "playlistId" : my_playlist_id,
                    "resourceId" : {
                        "kind" : "youtube#video",
                        "videoId" : response2['items'][i]['snippet']['resourceId']['videoId']
                    }
                }
            }
        )
        request2.execute()

def create_whole_playlist(youtube,playlist_id,my_channel_id) :
    name = input("Please name the PlayList :" + "\n")
    privacy = input("Private or Public ?" + "\n")
    request = youtube.playlists().insert(
        part = "snippet,status",
        body = {
            "snippet" : {
                "title" : name,
            },
            "status" : {
                "privacyStatus" : privacy
            }
        }
    )
    request.execute()

    sleep(2)
    request2 = youtube.playlistItems().list(
        part = "snippet",
        maxResults = 50,
        playlistId = playlist_id
    )
    response2 = request2.execute()
    new_playlist_id = find_playlistId(youtube,name,my_channel_id)
    for i in range(len(response2['items'])) :
        request3 = youtube.playlistItems().insert(
            part = "snippet",
            body = {
                "snippet" : {
                    "playlistId" : new_playlist_id,
                    "resourceId" : {
                        "kind" : "youtube#video",
                        "videoId" : response2['items'][i]['snippet']['resourceId']['videoId']
                    }
                }
            }
        )
        request3.execute()

def merge_playlist(youtube,my_channel_id) :
    playlist_id = list()
    with open('data.txt','r',encoding = 'utf-8') as f :
        url = f.readlines()
    for i in range(len(url)) :
        key = re.search('list=\S{34}',url[i])
        playlist_id.append(key.group()[5:])
    for i in range(len(url)) :
        request1 = youtube.playlistItems().list(
            part = "snippet",
            maxResults = 50,
            playlistId = playlist_id[i]
        )
        response1 = request1.execute()
        channel_id = response1['items'][0]['snippet']['channelId']

        request2 = youtube.playlists().list(
            part = "snippet",
            channelId = channel_id,
            maxResults = 50
        )
        response2 = request2.execute()
        print("-" * 50)
        for j in range(len(response2['items'])) :
            if response2['items'][j]['id'] == playlist_id[i] :
                print(f"{i + 1}. " + response2['items'][j]['snippet']['title'])
        print("-" * 50)

        print("A. Choose existing Playlist" + "\n" + "B. Create new Playlist")
        print("-" * 50)
        choose = input()
        if choose == 'A' :
            add_whole_playlist(youtube,playlist_id[i],my_channel_id)
        elif choose == 'B' :
            create_whole_playlist(youtube,playlist_id[i],my_channel_id)
        print("Succeeded!")
        print("=" * 50)

def commad_table() :
    table = dict()
    table = {
        1 : "新增影片到播放清單" , 2 : "刪除播放清單中的影片" , 3 : "查詢頻道內的影片" ,
        4 : "更改影片在播放清單的順序" , 5 : "將影片移到另個播放清單"  , 6 : "創建播放清單" ,
        7 : "刪除播放清單" , 8 : "頻道概覽" , 9 : "搬移整個播放清單到自己的頻道"
    }
    print("=" * 50)
    for key in table :
        print(key , "\t" , ":" ,table[key])
    print("=" * 50)

def main(credentials):
    credentials = create_forever_credentials(credentials)
    youtube = create_youtube(credentials)
    channel_id = "UC9yO_oXBU9rArKKhV2R3fiA"
    try :
        while True :
            commad_table()
            command = input("What do you want to do ?" + "\n")
            if command == "1" :
                add_video(youtube,channel_id)
            elif command == "2" :
                delete_video(youtube,channel_id)
            elif command == "3" :
                playlist_name = input("Which PlayList ? (Please input PlayList Name)"  + "\n")
                playlist_id = find_playlistId(youtube,playlist_name,channel_id)
                if playlist_id == 0 :
                    print("Sorry,playlist doesn't exist")
                else :
                    target = input("Please input video's URL or NAME :"  + "\n")
                    search_video(youtube,playlist_id,target)
            elif command == "4" :
                change_video_sequence(youtube,channel_id)
            elif command == "5" :
                move_video_to_another_playlist(youtube,channel_id)
            elif command == "6" :
                create_playlist(youtube,channel_id)
            elif command == "7" :
                delete_playlist(youtube,channel_id)
            elif command == "8" :
                channel_overview(youtube)
            elif command == '9' :
                print("Please input the PlayList URL in data.txt")
                start = input("Input OK to Start :" + "\n")
                if start == 'OK' :
                    merge_playlist(youtube,channel_id)
    except EOFError :
        pass

if __name__  == '__main__' :
    main(credentials)