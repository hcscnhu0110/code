import pandas as pd

def main() :
    with open('song_name.txt' , 'r' , encoding = 'utf-8') as f :
        song = f.readlines()
    with open('artist_name.txt' , 'r' , encoding = 'utf-8') as f :
        artist = f.readlines()
    with open('duration.txt' , 'r' , encoding = 'utf-8') as f :
        time = f.readlines()
    for i in range(len(song)) :
        if ',' in song[i] :
            song[i] = song[i].replace(',' , '&')
        song[i] = song[i].rstrip('\n')
        artist[i] = artist[i].rstrip('\n')
        time[i] = time[i].rstrip('\n')
    data = {'song' : song,
            'artist' : artist,
            'time' : time
    }
    #num = [i for i in range(1,9997)]
    dataframe = pd.DataFrame(data)
    dataframe.to_csv('info.csv' , index = False ,encoding = 'utf-8')

if __name__ == '__main__' :
    main()
