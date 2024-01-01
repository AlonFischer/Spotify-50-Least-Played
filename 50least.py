import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
import webbrowser


def get_spotify():
    #GET SPOTIFY API CREDENTIALS
    with open("secrets.json", "r") as f:
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
        print("got token")
        print(token)
    else:
        print("Can't get token")


get_spotify()