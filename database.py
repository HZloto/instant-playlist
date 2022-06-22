# Create csv of database
# - Spotify API
# - Output: pandas df or array with songs and their Spotify features
# CHRIS

## 1 ## Start with the output of the scrapper.py (a list of 49 artists)

scrapper_output = ['Purple Disco Machine', 'Claptone', 'Tensnake', 'Bellaire', 
                   'Tiger And Woods', 'Teenage Mutants', 'Crazy P', 'Drop Out Orchestra', 'Luke Solomon', 
                   'Hot Toddy', 'Art Of Tones', 'Teensnake', 'Horse Meat Disco', 'Made To Move', 
                   'Gavinco', 'Angelo Ferreri', 'Coeo', 'David Penn', 'Dimitri From Paris', 'Block & Crown', 
                   'Session Victim', 'Platinum Doug', 'Samishi', 'Leon Vynehall', 'Late Nite Tuff Guy', 'DeMarzo',
                   'Adryiano', 'Sidney Charles', 'Crazibiza', 'Rene Amesz', 'Black Loops',
                   'Lars Moston', 'Max Graef', 'Antonio Giacca', 'Nhan Solo', 'Superlover', 'JKriv',
                   'Kevin McKay', 'Robosonic', 'Harvey Sutherland', 'Antal', 'Dr Packer', 'Maceo Plex',
                   'The Cube Guys', 'Soundstream', 'Rockers Revenge', 'Fatnotronic', 'Mousse T', 
                   'Sonny Fodera']

## 2 ## Define function to get access tokens to Spotify API using credentials

import requests

def api_fetch(client_id='e665d5d853914ec2a5fa7a45fcf41b8c', client_secret='d34be89a80fa48c6b015f86b621514e3'):
    """
    Function that accesses the various endpoints of the Spotify API by passing an access token from client credentials.
    
    Param:
    -----
    - client_id: a string containining id to access app created in Spotify for Developers
    - client_secret: a string containing secret to access app created in Spotify for Developers

    Output:
    ------
    - headers
    """ 

    # URL for token resource
    auth_url = 'https://accounts.spotify.com/api/token'

    # Request body
    params = {'grant_type': 'client_credentials',
              'client_id': client_id,
              'client_secret': client_secret}

    # POST the request
    auth_response = requests.post(auth_url, params).json()

    # Retrieve the access token
    access_token = auth_response['access_token']

    # Save the header in a new variable so you can use it later on
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    
    return headers

# Call the function to save the header in a new variable
headers = api_fetch()

## 3 ## Use the Spotify API (check SpotiPy library for help) to find their 5 most popular song for each artist

def top_n_tracks():
    """
    Function that scraps the API of Spotify to get the top N tracks of the artists scrapped in scrapper.py and the corresponding features.

    Param:
    -----
    - n: int. Any integer between 1 and 10. Default value is 5.    

    Output:
    ------
    - track_ids, track_titles, artist_names
    - danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo
    """

    ### Get above artists' IDs to be able to get tracks of each artist

    # Define base url
    base_url = 'https://api.spotify.com/v1/'

    # Initialize track id list
    track_ids, track_titles, artist_names = ([] for i in range(3))

    # Create loop to get artist id and then get the top n tracks of the corresponding artist
    for artist_name in scrapper_output:
        artist_search_endpoint = base_url + 'search?q=' + artist_name.replace(' ', '%20') + '&type=artist'
        artist_id = requests.get(artist_search_endpoint, headers=headers).json()['artists']['items'][0]['id']
        artist_top_tracks_endpoint = base_url + 'artists/' + artist_id + '/top-tracks?market=ES'
        track_info = requests.get(artist_top_tracks_endpoint, headers=headers).json()['tracks']
        for i in range(len(track_info)):
            track_ids.append(track_info[i]['id'])
            track_titles.append(track_info[i]['name'])
            artist_names.append(track_info[i]['artists'][0]['name'])

    ### Get all other features of each track

    # Initialize the lists
    danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo = \
    ([] for i in range(10))

    # Set the audio features endpoint
    audio_features_endpoint = base_url + 'audio-features'

    # Create a loop and use the audio features endpoint to fetch the above features and append them to lists above
    for track_id in track_ids:

        # Get the GET Audio Features request
        track_info = requests.get(audio_features_endpoint, headers=headers, params={'ids': track_id}).json()

        # Get the audio features subset
        track_info_features = track_info['audio_features'][0]

        # Append the features' values
        danceability.append(track_info_features['danceability'])
        energy.append(track_info_features['energy'])
        loudness.append(track_info_features['loudness'])
        mode.append(track_info_features['mode'])
        speechiness.append(track_info_features['speechiness'])
        acousticness.append(track_info_features['acousticness'])
        instrumentalness.append(track_info_features['instrumentalness'])
        liveness.append(track_info_features['liveness'])
        valence.append(track_info_features['valence'])
        tempo.append(track_info_features['tempo'])

    return track_ids, track_titles, artist_names, \
           danceability, energy, loudness, mode, speechiness, acousticness, \
           instrumentalness, liveness, valence, tempo

## 4 ## Create a df with these columns: song id, title, artist, and all features (['danceability', 'energy', 'loudness', 'mode', 'speechiness',
#      'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']) 
#       The df should contain about 245 songs (49 artistsx5)

# Importing pandas library
import pandas as pd 
    
def create_database(track_features=top_n_tracks()):
    """
    Function that gets the features of the tracks in list form and returns a named dataframe.

    Param:
    -----
    - track_features: function or lists. All the features of a track that will be used in the recommender system.    

    Output:
    ------
    - df
    """

    # Get the track features
    track_ids, track_titles, artist_names, \
    danceability, energy, loudness, mode, speechiness, acousticness, \
    instrumentalness, liveness, valence, tempo = track_features

    # Dictionary of lists 
    track_dict = {'id': track_ids, 'title': track_titles, 'artist': artist_names, 
                  'danceability': danceability, 'energy': energy, 'loudness': loudness, 'mode': mode, 
                  'speechiness': speechiness, 'acousticness': acousticness, 'instrumentalness': instrumentalness, 
                  'liveness': liveness, 'valence': valence, 'tempo': tempo} 

    # Create dataframe
    df = pd.DataFrame(track_dict)

    # Print dataframe
    return df 

### Return the dataframe
create_database()