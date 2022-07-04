import pandas as pd
import scipy
import scipy.spatial

def pick_closest_songs(df_song_input: pd.DataFrame, df_target: pd.DataFrame) -> list:
    '''
    This function picks the closest song to an input song for evey artist in a dataframe using spotify analysis
    
    Param:
    -----
    - df_song_input: a pandas dataframe with one row
    - df_target: a pandas dataframe with many songs from different artists 

    Output:
    ------
    - List of spotify track ids 
    
    '''
    
    #Create list of all individual artists in the target df
    art_list = list(set(df_target['artist']))
    
    #Only keep numerical variables
    df_song_input = df_song_input[['id','danceability', 'energy', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]

    #Initialize empty output list
    output_tracks_list = []

    for i in art_list:
        
        #We iterate artist by artist, creating a df for each with only their songs
        temp_df = df_target[df_target['artist'] == str(i)]
        
        #Only keep numerical variables
        temp_df_1 = temp_df[['id','danceability', 'energy', 'loudness', 'mode', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]
        
        #use spacial distance to identify closest song to our input
        ary = scipy.spatial.distance.cdist(df_song_input.drop(columns=['id']), temp_df_1.drop(columns=['id']), metric='euclidean')
        ary = ary[0].tolist()
        
        #Find the minimum value (closest)
        minimum = min(ary)
        
        #Get the index position of the closest song
        out_index = ary.index(minimum)
        
        #append ID of closest song to our output list
        output_tracks_list.append(temp_df_1.iloc[out_index]['id'])
        
    return output_tracks_list