# Recommender to find similar songs:
# - Some library (not sure yet, autoencoders?) 
# - Compare song output with our database csv
# - Output: List of top 10 songs in terms of similarities (define how we value similarity)
# HUGO
#Random text

# 1. give spotify song id
# 2. give a csv
# 3. return the 10 closest songs

#IMPORTS
import pandas as pd
import requests
import scipy
import scipy.spatial



def get_song_features(song_id: str, client_id: str = "f0affaf409354cc89102c9ff41044fe4", client_secret: str = "f61d4df574404456ace1ba73551ce432") -> pd.DataFrame:
    '''
    
    This fuction takes a song spotify ID and returns a pandas dataframe with its features
    
    '''


    # URL for token resource
    auth_url = 'https://accounts.spotify.com/api/token'

    # request body
    params = {'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret}

    # POST the request
    auth_response = requests.post(auth_url, params).json()
    
    # Retreive token
    access_token = auth_response['access_token']
    access_token 

    #headers
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

    #URL
    base_url = 'https://api.spotify.com/v1/'

    # audio features endpoint
    endpoint = "audio-features"
    audio_features_endpoint = base_url + endpoint
    audio_features_endpoint

    #params
    params = {"ids" : song_id} 

    url = audio_features_endpoint
    song_attributes = requests.get(url, headers = headers , params = params).json()

    df_song_input = pd.DataFrame(song_attributes["audio_features"])
    df_song_input = df_song_input[['danceability', 'energy', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo','id']]
    return df_song_input

def get_target_df(df_target_path: str = 'temp_recommender.csv') -> pd.DataFrame:
    '''
    
    This fuction takes the csv path of a list of spotify song features and returns a pandas dataframe.
    
    '''

    df_target = pd.read_csv(df_target_path)
    df_target = df_target[['danceability', 'energy', 'loudness', 'mode', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo','track_id']]
    df_target = df_target.rename(columns={'track_id':'id'})
    return df_target


df_song_input = get_song_features(song_id = '2QuSUJTRJMzWssW9nXPGcf') # Id of the spotify target sound
df_target = get_target_df(df_target_path = 'temp_recommender.csv')


ary = scipy.spatial.distance.cdist(df_song_input.drop(columns=['id']), df_target.drop(columns=['id']), metric='euclidean')
print(df_song_input[ary==ary.min()])