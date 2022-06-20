import html_to_json
import requests 

def url_maker(artist_name = "matthieu faubourg"):
    base_url = 'https://www.music-map.com/'
    mylist = artist_name.split(' ')
    end_url = ""
    if len(mylist) == 1:
        end_url = mylist[0] 
        final_url = base_url + end_url
        return final_url
    else:
        for i in range(len(mylist)):
            end_url = end_url+mylist[i]+'+'
        final_url = base_url + end_url
        return final_url


html_string = requests.get(url_maker(artist_name = input("artist?"))).text


output_json = html_to_json.convert(html_string)
res = output_json['html'][0]['body'][0]['table'][0]['tr'][0]['tr'][0]['td'][0]['div'][1]['a']

for i in range(len(res)):
    print(res[i]['_value'])
