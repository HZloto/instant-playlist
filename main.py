import requests
from scrapper import Scrapper
import pandas as pd
import random
import time
import pandas as pd


def api_fetch(client_id: str ='e665d5d853914ec2a5fa7a45fcf41b8c', client_secret: str ='d34be89a80fa48c6b015f86b621514e3') -> dict:
    """
    Function that accesses the various endpoints of the Spotify API by passing an access token from client credentials.
    
    Param:
    -----
    - client_id: a string containining id to access app created in Spotify for Developers
    - client_secret: a string containing secret to access app created in Spotify for Developers

    Output:
    ------
    - headers dictionnary 
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


def top_n_tracks(scrapper_output: list) -> pd.DataFrame:
    """
    Function that scraps the API of Spotify to get the top 5 tracks of the artists scrapped in scrapper.py and the corresponding features.
    If the artist has less than 5 tracks on Spotify, it returns all of his discography.
    
    Param:
    -----
    - scrapper_output: list of artists output by the scapper    

    Output:
    ------
    Pandas DataFrame with:
    - track_ids, track_titles, artist_names
    - danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo
    """
   
    
    # Call the function to save the header in a new variable
    headers = api_fetch()

    ### Get above artists' IDs to be able to get tracks of each artist

    # Define base url
    base_url = 'https://api.spotify.com/v1/'

    # Initialize track id list
    track_ids, track_titles, artist_names = ([] for i in range(3))

    # Create loop to get artist id and then get the top n tracks of the corresponding artist
    for artist_name in scrapper_output:
        artist_search_endpoint = base_url + 'search?q=' + artist_name.replace(' ', '%20') + '&type=artist'
        
        try:
            artist_id = requests.get(artist_search_endpoint, headers=headers).json()['artists']['items'][0]['id']
            artist_top_tracks_endpoint = base_url + 'artists/' + artist_id + '/top-tracks?market=ES'
            track_info = requests.get(artist_top_tracks_endpoint, headers=headers).json()['tracks']
            print("getting top tracks for: ", artist_name,"...")
            for i in range(min(5, int(len(track_info)))):
                track_ids.append(track_info[i]['id'])
                track_titles.append(track_info[i]['name'])
                artist_names.append(track_info[i]['artists'][0]['name'])
        except:
            pass
        
    ### Get all other features of each track

    # Initialize the lists
    danceability, energy, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo = \
    ([] for i in range(10))

    # Set the audio features endpoint
    audio_features_endpoint = base_url + 'audio-features'

    # Create a loop and use the audio features endpoint to fetch the above features and append them to lists above
    counter = 0
    for track_id in track_ids:

        # Get the GET Audio Features request
        track_info = requests.get(audio_features_endpoint, headers=headers, params={'ids': track_id}).json()
        counter += 1 
        if counter == 30:
            time.sleep(0.5)
            counter = 0 
        else:
            pass

        # Get the audio features subset
        print(track_info)
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

    
def create_database(scrapper_output: list) -> pd.DataFrame:
    """
    Function that gets the features of the tracks in list form and returns a named dataframe.

    Param:
    -----
    - track_features: function or lists. All the features of a track that will be used in the recommender system.    

    Output:
    ------
    - df
    """
    
    track_features=top_n_tracks(scrapper_output)

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


def make_dataframe(artist_name: str, save_csv: bool = False) -> pd.DataFrame:
    '''
    For a given artist name, returns a dataframe with 245 tracks of similar artists.
    
    Params
    ------
    - artist name: name of the artist
    - save_csv: Bool to pick if user wants a csv copy saved
    
    Output
    ------
    - Pandas Dataframe
    - Artist name
    
    '''

    #Initiate the scrapper class
    scrapper = Scrapper()

    #Call the get_similar_artists function
    scrapper_output = scrapper.get_similar_artists(artist_name= artist_name)

    df = create_database(scrapper_output=scrapper_output)
    
    if save_csv == True:
        df.to_csv(f'{artist_name}_based_playlist.csv')
        return df
    else:
        return df    
    
