# Create csv of database
# - Spotify API
# - Output: pandas df or array with songs and their Spotify features
# CHRIS

#1. Start with the output of the scrapper.py (a list of 49 artists)
## Here is an example of the scrapper output so you can work on it before it's ready
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

#2. Use the Spotify API (check SpotiPy library for help) to find their 5 most popular song for each artist

#3. Create a df with these columns: song id, title, artist, and all features (['danceability', 'energy', 'loudness', 'mode', 'speechiness',
#   'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']) 
# The df should contain about 245 songs (49 artistsx5)