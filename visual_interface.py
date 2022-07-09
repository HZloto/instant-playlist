import streamlit as st
import time
import random
from playlist_api import create_playlist
from input_api import top_track_df_1, top_track_df_2
from recommender import pick_closest_songs
from main import make_dataframe

# For the app to be stateful, we first check if our variables already exist
if 'artist' not in st.session_state: 
    st.session_state.artist = False 
    
if 'test' not in st.session_state:
    st.session_state.test = False
    
# Visuals  
title = "Song Recommendation Engine"
st.title(title)

# Visuals
st.subheader('Created by: APP Group H')
st.write('Welcome to our Song Recommendation Engine, created for Advanced Programming in Python')
    
# If the variables are filled (the user already filled the form, we show a progress bar and call our scripts)
if st.session_state.test != False:
    my_bar = st.progress(0)
    st.write("Go get a coffee! We're working on it.")
    
    for percent_complete in range(100):
        time.sleep(random.uniform(0,0.1))
        my_bar.progress(percent_complete + 1)

        # We call different parts of the scripts throughout the loading
        if percent_complete == 30:
            playlist_df = make_dataframe(artist_name = st.session_state.artist, save_csv = False )
            
        if percent_complete == 70:    
            song_list = pick_closest_songs(df_song_input = top_track_df_2(st.session_state.artist, st.session_state.test[0]), df_target=playlist_df)
            playlist_name = f"Your {st.session_state.artist} inspired playlist"
            URL = create_playlist(songs_id_list=song_list, playlist_name=playlist_name)
    
    # Visuals        
    st.subheader('Your playlist is ready!')
    st.markdown("We have generated your Spotify playlist:")
    st.subheader(URL)
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.write("##")
    st.subheader('Want to try again? Down here!')
    
# First part of the app is the users sees it for the first time    
st.write('You can insert the name of the artist you like in the box, and we will create a playlist for you inspired on their songs!')
st.markdown("##") 
    
with st.form("my_form"):
    # Input the artist name
    artist_name = st.text_input("Name of the artist:")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    
if submitted:
    # Once the first button is clicked, we call the Spotify API to get the top 10 tracks and get the user to pick one
    st.session_state.artist = artist_name
    disp_list = ["PICK ONE"] + top_track_df_1(st.session_state.artist)
    
    # Visuals  
    st.write(f'Based on {st.session_state.artist}, please select one of the 10 displayed songs you would like your playlist to be based on:')
    st.selectbox('Choose a song here',disp_list, key = 'test')
