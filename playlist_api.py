# API call to create public playlist with the songs.
# - Create a public playlist with bot
# - Output: URL of playlist
# 1. You will get a list of 50 Spotify song IDs

# 2. Create an API call to Spotify (SpotiPy can help) to create a public playlist
# (check if we can create a free spotify account to do so)

# 3. Return the URL to the playlist
from os import access
import spotipy
from spotipy.oauth2 import SpotifyOAuth
#Create connection class
# class connection():
#     def __init__(self) -> None:   
#         self.__username = '31zso72caup6z433kx5z5tr6tfcq'
#         self.__client_id='f0affaf409354cc89102c9ff41044fe4'
#         self.__client_secret='f61d4df574404456ace1ba73551ce432'
#         self.__redirect_uri='http://127.0.0.1:9090'
#         self.__scope="playlist-modify-public, playlist-modify-private, user-library-read, user-top-read"

    
#     def get_acces(self):
#         self.__token = SpotifyOAuth(client_id=self.__client_id,
#                             client_secret=self.__client_secret,
#                             scope=self.__scope, username=self.__username,
#                             redirect_uri=self.__redirect_uri)
    

#         spotifyObject = spotipy.Spotify(auth_manager = self.__token)
#         return spotifyObject,self.__username





#songs_id_list = ['6Sq7ltF9Qa7SNFBsV5Cogx','3k3NWokhRRkEPhCzPmV8TW','77JW5yocR1NgteaKKLweQP']
def create_playlist(songs_id_list,playlist_name):
    
    client_id = "f0affaf409354cc89102c9ff41044fe4"
    client_secret = "f61d4df574404456ace1ba73551ce432"
    redirect_uri = 'http://127.0.0.1:9090'
    scope = "playlist-modify-public, playlist-modify-private, user-library-read, user-top-read"
    username = "31zso72caup6z433kx5z5tr6tfcq"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret= client_secret, redirect_uri=redirect_uri, username = username, scope=scope))

    #Make the conection
    playlist_name = str(playlist_name)
    spotifyObject = sp
    

    #create playlist
    spotifyObject.user_playlist_create(user=username, name=playlist_name)
    #find the new playlist created
    prePlaylist = spotifyObject.user_playlists(user=username) 
    # get the id of the last list created( the [0] is the part of the code that take the last list)
    playlist = prePlaylist ['items'][0]['id']
    # get the id of the last list created( the [0] is the part of the code that take the last list)
    playlist_url = prePlaylist['items'][0]['external_urls']['spotify']
    #add songs to the 
    spotifyObject.user_playlist_add_tracks (user=username, playlist_id=playlist, tracks=songs_id_list)
    return playlist_url
    
#create_playlist(songs_id_list=songs_id_list)