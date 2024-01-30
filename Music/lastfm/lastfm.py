from typing import List
import requests
import json
from song import Song

def get_lastfm_top_tracks() -> List[Song]:
    #define headers and URL
    page = 1
    limit = 1000

    with open("./Music/lastfm/lastfmSecrets.json", "r") as f:
        credentials = json.load(f)

    print("Getting LastFM Top Tracks")

    headers = { 'user-agent': credentials["LastFM_USER_AGENT"]}
    topTracks = list()
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
            tracksAsSongs = [Song(t['name'], t['artist']['name'], t['playcount']) for t in response.json()['toptracks']['track']]
            topTracks.extend(tracksAsSongs)
        else:
            print("DONE")
            break
    
    return topTracks
