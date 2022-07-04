import streamlit as st
import time
import pandas as pd
import random

title = "Song Recommendation Engine"
st.title(title)

# with st.container():
#     col1, col2 = st.columns((5,1))
#     with col1:
        
st.subheader('Created by: APP Group H')
st.write('Welcome to our Song Recommendation Engine, created for Advanced Programming in Python')
st.write('You can insert the name of the artist you like in the box, and we will create a playlist for you inspired on their songs!')
st.markdown("##")   

col1, col2 = st.columns(2)
col1.subheader('Insert an artist to your liking')
#col2.subheader('Check 2')
# 
songs = []          
with st.form("my_form"):
    #st.write("Inside the form")
    artist_name = st.text_input("Name of the artist:")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        #st.write(main(artist_name))
        st.markdown(f'Your chosen artist name is: {artist_name}')

# if submitted:
    #time.sleep(1)
st.markdown("##")        
st.write('Based on your chosen artist, please select one of the 10 displayed songs you would like your playlist to be based on:')

#if its in the with, then its in the form and that is ugly
#if submitted:
songs = ['Pick a song', 'Wannabe', 'Stop', 'Spice Up Your Life', "Say You'll Be There", '2 Become 1', 'Who Do You Think You Are', 'Viva Forever', 'Mama', 'Too Much', 'Goodbye']
    # songs = pd.DataFrame()
    # songs['songs'] = song_list
favorite_song = st.selectbox('Choose the song you like the most at the moment', options = songs)

#st.write('Current selection:', favorite_song)


# favorite_song = st.selectbox('Choose the song you like the most at the moment', options = songs_list)
  



buffer1, col1, buffer2 = st.columns([1.45, 1, 1])
is_clicked = col1.button(label="Recommend")

if is_clicked:
    st.markdown("##") 
    st.markdown("##")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(random.uniform(0,0.1))
        my_bar.progress(percent_complete + 1)
    st.subheader('Your playlist is ready!')
    playlist_url = 'https://open.spotify.com/playlist/3lunKl2popziIftRIhjrRR'
    st.write('The URL is:', playlist_url)
    st.markdown("##") 
    st.write('If you click on it, a playlist specially created for you will be displayed.')

#if favorite_song:
    #st.markdown("##") 
    #st.markdown("##") 
    #st.subheader('Your playlist is ready!')
    #playlist_url = 'https://open.spotify.com/playlist/3lunKl2popziIftRIhjrRR'
    #st.write('The URL is:', playlist_url)
    #st.markdown("##") 
    #st.write('If you click on it, a playlist specially created for you will be displayed.')







#st.write("Outside the form")
# st.header('Insert an artist to your liking')









