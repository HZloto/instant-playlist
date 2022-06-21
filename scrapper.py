import html_to_json
import requests 

def url_maker(artist_name = "matthieu faubourg"):
    '''
    
    This function generates the url to get the similar artists. 
    
    
    '''
    
    #Define base url 
    base_url = 'https://www.music-map.com/'
    
    #Splits all the words by blank space
    artist_name_elements = artist_name.split(' ')
    
    #initiate end_url
    end_url = ""
    
    #If the artist has a one word name, we append it to the base url
    if len(artist_name_elements) == 1:
        end_url = artist_name_elements[0] 
        final_url = base_url + end_url
        return final_url
    
    #If it has more than one word, we iterate one by one through the list
    ##To build the URL
    else:
        for i in range(len(artist_name_elements)):
            end_url = end_url+artist_name_elements[i]+'+'
        final_url = base_url + end_url
        return final_url


def get_similar_artists(artist_name = url_maker(artist_name = input("ENTER ARTIST NAME:  "))):
    
    #Make the request to the website to get html
    html_string = requests.get(artist_name).text

    #Convert the html to json
    output_json = html_to_json.convert(html_string)

    #Parse the json to get to the artist names
    res = output_json['html'][0]['body'][0]['table'][0]['tr'][0]['tr'][0]['td'][0]['div'][1]['a']

    #Initiate empty list
    similar_artists = []
    for i in range(len(res)):
        similar_artists.append(res[i]['_value'])
    
    return similar_artists


print(get_similar_artists())

xxxx
