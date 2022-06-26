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
class connection():
    def __init__(self) -> None:   
        self.__username = '31zso72caup6z433kx5z5tr6tfcq'
        self.__client_id='015d0e27d03444f495901395b380148d'
        self.__client_secret='8aa03f138bcc442097b11a6d34b4be09'
        self.__redirect_uri='http://127.0.0.1:8080/'
        self.__scope='playlist-modify-public'

    
    def get_acces(self):
        self.__token = SpotifyOAuth(client_id=self.__client_id,
                            client_secret=self.__client_secret,
                            scope=self.__scope, username=self.__username,
                            redirect_uri=self.__redirect_uri)
    

        spotifyObject = spotipy.Spotify(auth_manager = self.__token)
        return spotifyObject,self.__username

songs_id_list = ['6Sq7ltF9Qa7SNFBsV5Cogx','3k3NWokhRRkEPhCzPmV8TW','77JW5yocR1NgteaKKLweQP']
def create_playlist(songs_id_list):
    
    #Make the conection
    playlist_name = 'Your top 50 songs'
    conn=connection()
    acces=conn.get_acces()
    spotifyObject=acces[0]
    __username=acces[1]

    #create playlist
    spotifyObject.user_playlist_create(user=__username, name=playlist_name)
    #find the new playlist created
    prePlaylist = spotifyObject.user_playlists(user=__username) 
    # get the id of the last list created( the [0] is the part of the code that take the last list)
    playlist = prePlaylist ['items'][0]['id']
    # get the id of the last list created( the [0] is the part of the code that take the last list)
    playlist_url = prePlaylist['items'][0]['external_urls']['spotify']
    #add songs to the 
    spotifyObject.user_playlist_add_tracks (user=__username, playlist_id=playlist, tracks=songs_id_list)
    return playlist_url
    
create_playlist(songs_id_list=songs_id_list)