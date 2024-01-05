from typing import List
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
import webbrowser


def get_spotify_token() -> str:
    #GET SPOTIFY API CREDENTIALS
    with open("./spotify/spotifySecrets.json", "r") as f:
        credentials = json.load(f)

    os.environ["SPOTIPY_CLIENT_ID"] = credentials["Spotify_Client_ID"]
    os.environ["SPOTIPY_CLIENT_SECRET"] = credentials["Spotify_Client_Secret"]
    os.environ["SPOTIPY_REDIRECT_URI"] = credentials["Spotify_Redirect_Url"]
    SCOPE = 'user-library-read playlist-modify-public'


    #GET SPOTIFY TOKEN
    token = spotipy.util.prompt_for_user_token(credentials["Spotify_Client_ID"], SCOPE)

    login = "https://accounts.spotify.com/authorize?scope=" + SCOPE + "&redirect_uri=" + credentials["Spotify_Redirect_Url"] + "&response_type=code&client_id=" + credentials["Spotify_Client_ID"]
    webbrowser.open(login)

    if token:
        return token
    else:
        print("Can't get token")

def get_spotify_saved_songs(token: str) -> List:
    if token == "":
        print("Token cannot be empty")
        return
    
    sp = spotipy.Spotify(auth=token)
    offset = 0
    
    print("Getting all Spotify Saved Songs")

    #################################
    #TODO see if this can be sped up#
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    totalSongs = results['total']
    while results['next']:
        print('----Loaded ' + str(len(tracks)) + " / " + str(totalSongs) + '----')
        results = sp.next(results)
        tracks.extend(results['items'])
    for idx, item in enumerate(tracks):
        track = item['track']
        print(idx, track['artists'][0]['name'], " - ", track['name'])
    #################################

    #Test log
    print('Total Songs - ', len(tracks))
    print(type(tracks))