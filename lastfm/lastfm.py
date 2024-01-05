import requests
import json

def get_lastfm_top_tracks():
    #define headers and URL
    page = 1
    limit = 1000

    with open("./lastfm/lastfmSecrets.json", "r") as f:
        credentials = json.load(f)

    print("Getting LastFM Top Tracks")

    headers = { 'user-agent': credentials["LastFM_USER_AGENT"]}
    while(True):
        payload = {
			'api_key': credentials["LastFM_API_KEY"],
			'user': 'Ace6909',
			'period': 'overall',
			'page': page,
			'limit': limit,
			'method': 'user.gettoptracks',
			'format': 'json'
		}

        response = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
        if response.json()['toptracks']['track']:
            print("Found: " + str(page * limit) + " / " + str(response.json()['toptracks']['@attr']['total']) + " songs")
            page += 1
        else:
            print("DONE")
            break
            