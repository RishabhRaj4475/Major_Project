import requests
import json
def get_loc():
    send_url = "http://api.ipstack.com/check?access_key=fd03b9fc72fbadbf4518cf537f547987"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    loc=str(latitude)+","+str(longitude)
    return loc
#print("location==",get_loc())
