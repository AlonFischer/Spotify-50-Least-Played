import requests
import json

#TODO fix this, import from parent class
import sys
sys.path.append("...")

from ... import *

def get_lastfm_top_tracks():
    #define headers and URL
    page = 1
    limit = 1000

    with open("./lastfm/lastfmSecrets.json", "r") as f:
        credentials = json.load(f)

    print("Getting LastFM Top Tracks")

    headers = { 'user-agent': credentials["LastFM_USER_AGENT"]}
    topTracks = []
    print(topTracks)
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
            track = response.json()['toptracks']['track'][0]
            print(track)
            topTracks.append(Song(track['artist'], track['name'], track['playcount']) for track in response.json()['toptracks']['track'])
        else:
            print("DONE")
            break

        print(topTracks[0])
