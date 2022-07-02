# API call for input
# - Spotify API
# - Output: vector/list/array with all the song’s features
# MARTIN
# 1. Create a function that takes as an input the name of one artist
# (We only ask for artist name for simplicity)

# 2. Make a spotify API call (SpotiPy can help) to get the artist's most popular song

# 3.return artist name as a string and best song as a df with the following features:
# ['danceability', 'energy', 'loudness', 'mode', 'speechiness',
#   'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

import requests
import pandas as pd

class connection():
    def __init__(self) -> None:
        self.__client_id = "6501d860b4b34349b45b2af4b1d9b5c9"
        self.__client_secret = "e034edd0be29447e90914e512e359625"

    def get_auth(self):
        auth_url = 'https://accounts.spotify.com/api/token'
        params = {'grant_type': 'client_credentials', 'client_id': self.__client_id,
                  'client_secret': self.__client_secret}

        auth_response = requests.post(auth_url, params).json()
        access_token = auth_response["access_token"]
        headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
        return headers


def get_artist_top_track(artist_name):

    #Create the connection to spotify API Based on the customer input
    connect_instance = connection()
    headers = connect_instance.get_auth()

    #defining params and endpoint
    url = 'https://api.spotify.com/v1/search?'
    params = {'q':artist_name, 'type':'artist'}

    #Call the API to get the Artist ID first
    artist_id = str(requests.get(url, headers=headers, params=params).json()['artists'][
        'items'][0]['id'])

    #Make another call to the api with the artist ID to Artist top track

    #We define the url of the API and the params to be passed
    url2 = 'https://api.spotify.com/v1/artists/' + artist_id + "/top-tracks"
    params2 = {'id': artist_id, 'market':'ES'}

    #Make the API call and store two results, top_track and top_traci_id
    top_track_json = requests.get(url2, headers = headers, params =params2).json()
    top_track=[]
    top_track_id=[]
    num_of_songs=len(top_track_json['tracks'])

    for i in range(0,num_of_songs):
        top_track.append((i,top_track_json['tracks'][i]['name']))
        top_track_id.append(top_track_json['tracks'][i]['id'])
        
    return top_track, top_track_id


def top_track_df(artist_name = "bellaire"):
    # We need the input from the user
    
    #artist_name = input('Write down your favorite artist: ')
    songs_list=get_artist_top_track(artist_name)[0]
    print(songs_list)
    favorite_song= input ('Write the number of your favorite song from the  list: ')

    top_track, top_track_id = get_artist_top_track(artist_name)
    

    # REquest tokens to connect to API
    connect_instance = connection()
    headers = connect_instance.get_auth()

    #Prepare for API:
    url = 'https://api.spotify.com/v1/audio-features/' + top_track_id[int(favorite_song)]
    params = {"id": top_track_id[int(favorite_song)]}

    #Call API
    features_json = requests.get(url, headers=headers, params=params).json()

    #Create Dataframe with song features
    df = pd.DataFrame(features_json, index = [0])
    df['artist'] = artist_name
    df['title'] = top_track[int(favorite_song)][1]
    df=df[['id', 'title', 'artist', 'danceability', 'energy',
       'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
       'liveness', 'valence', 'tempo']]

    return df


if __name__ == "__main__":

    a = top_track_df()
    a
