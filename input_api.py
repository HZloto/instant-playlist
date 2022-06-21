# API call for input
# - Spotify API
# - Output: vector/list/array with all the song’s features
# MARTIN
import requests

class connection():
    def __init__(self) -> None:
        self.__client_id = "6501d860b4b34349b45b2af4b1d9b5c9"
        self.__client_secret = "e034edd0be29447e90914e512e359625"

    def get_auth(self):
        

inp = input('Type your song')

# URL for token resource
auth_url = 'https://accounts.spotify.com/api/token'

# request body
params = {'grant_type': 'client_credentials',
          'client_id': client_id,
          'client_secret': client_secret}

# POST the request
auth_response = requests.post(auth_url, params).json()

# 1. Create a function that takes as an input the name of one artist
# (We only ask for artist name for simplicity)
test_artist = "Bad Bunny"

# 2. Make a spotify API call (SpotiPy can help) to get the artist's most popular song

# 3.return artist name as a string and best song as a df with the following features:
# ['danceability', 'energy', 'loudness', 'mode', 'speechiness',
#   'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
