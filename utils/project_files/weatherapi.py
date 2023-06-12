import requests


def weather(lat, long):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":f"{lat},{long}"}

    headers = {
	    "X-RapidAPI-Key": "1922465af5msh1d0215ce95242edp1395a0jsn2c936dd183aa",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    data = {}
    data['name'] = response['location']['name']
    data['region'] = response['location']['region']
    data['country'] = response['location']['country']
    data['text'] = response['current']['condition']['text']
    data['temp_c'] = response['current']['temp_c']
    data['wind'] = response['current']['wind_mph']
    data['wind_dir'] = response['current']['wind_dir']
    data['last_update_time'] = response['location']['localtime']

    # pprint(data)
    return data

# weather(40.9, 71.6)