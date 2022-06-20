# Recommender to find similar songs:
# - Some library (not sure yet, autoencoders?) 
# - Compare song output with our database csv
# - Output: List of top 10 songs in terms of similarities (define how we value similarity)
# HUGO

# 1. give spotify song id
# 2. give a csv
# 3. return the 10 closest songs

#IMPORTS
import pandas as pd
import requests

song_id = '2QuSUJTRJMzWssW9nXPGcf' # Id of the spotify target sound

def get_song_features(song_id: str = song_id, client_id: str = "069700c64b6d428088724522a691188c", client_secret: str = "3cb0e989241f47df8cc6f79a34f8ff8a") -> pd.DataFrame:
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
    return df_song_input


df_target = pd.read_csv('temp_recommender.csv')

print(get_song_features())