import spotipy
from spotipy.oauth2 import SpotifyOAuth

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
    
    # add songs 
    spotifyObject.user_playlist_add_tracks (user=username, playlist_id=playlist, tracks=songs_id_list)
    return playlist_url
