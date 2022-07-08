import streamlit as st
from input_api import top_track_df_1
import webbrowser
from scrapper import Scrapper
import pandas as pd
from playlist_api import create_playlist
from input_api import top_track_df_1, top_track_df_2
from recommender import pick_closest_songs
import streamlit as st
import time
import pandas as pd
import random
from scrapper import Scrapper
import pandas as pd
from playlist_api import create_playlist
from input_api import top_track_df_1, top_track_df_2
from recommender import pick_closest_songs
from main import make_dataframe

if 'artist' not in st.session_state: 
    st.session_state.artist = False 
    
if 'test' not in st.session_state:
    st.session_state.test = False
    
    
title = "Song Recommendation Engine"
st.title(title)


st.subheader('Created by: APP Group H')
st.write('Welcome to our Song Recommendation Engine, created for Advanced Programming in Python')
    
    
if st.session_state.test != False:
    my_bar = st.progress(0)
    st.write("Go get a coffee! We're working on it.")
    for percent_complete in range(100):
        time.sleep(random.uniform(0.3,0.9))
        my_bar.progress(percent_complete + 1)
    st.subheader('Your playlist is ready!')
    playlist_df = make_dataframe(artist_name = st.session_state.artist, save_csv = False )
    song_list = pick_closest_songs(df_song_input = top_track_df_2(st.session_state.artist, st.session_state.test[0]), df_target=playlist_df)
    playlist_name = f"Your {st.session_state.artist} inspired playlist"
    URL = create_playlist(songs_id_list=song_list, playlist_name=playlist_name)
    
    st.markdown("We have generated your Spotify playlist:")
    st.subheader(URL)
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    
    
    st.subheader('Want to try again? Down here!')
st.write('You can insert the name of the artist you like in the box, and we will create a playlist for you inspired on their songs!')
st.markdown("##") 
    
with st.form("my_form"):
    #st.write("Inside the form")
    artist_name = st.text_input("Name of the artist:")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    
if submitted:
    st.session_state.artist = artist_name
    st.markdown(f'Your chosen artist name is: {st.session_state.artist}')
    disp_list = ["PICK ONE"] + top_track_df_1(st.session_state.artist)
    
        
    st.write('Based on your chosen artist, please select one of the 10 displayed songs you would like your playlist to be based on:')
    st.selectbox('Choose a song here',disp_list, key = 'test')
