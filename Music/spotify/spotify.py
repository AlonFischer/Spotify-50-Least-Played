from typing import List
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
import webbrowser
from song import Song


def get_spotify_token() -> str:
    #GET SPOTIFY API CREDENTIALS
    with open("./Music/spotify/spotifySecrets.json", "r") as f:
        credentials = json.load(f)

    os.environ["SPOTIPY_CLIENT_ID"] = credentials["Spotify_Client_ID"]
    os.environ["SPOTIPY_CLIENT_SECRET"] = credentials["Spotify_Client_Secret"]
    os.environ["SPOTIPY_REDIRECT_URI"] = credentials["Spotify_Redirect_Url"]
    SCOPE = 'user-library-read playlist-modify-public playlist-modify-private'


    #GET SPOTIFY TOKEN
    token = spotipy.util.prompt_for_user_token(credentials["Spotify_Client_ID"], SCOPE)

    login = "https://accounts.spotify.com/authorize?scope=" + SCOPE + "&redirect_uri=" + credentials["Spotify_Redirect_Url"] + "&response_type=code&client_id=" + credentials["Spotify_Client_ID"]
    webbrowser.open(login)

    if token:
        return token
    else:
        print("Can't get token")

def get_spotify_saved_songs(token: str) -> List[Song]:
    if token == "":
        print("Token cannot be empty")
        return
    
    sp = spotipy.Spotify(auth=token)
    offset = 0
    
    print("Getting all Spotify Saved Songs")

    #################################
    #TODO see if this can be sped up#
    results = sp.current_user_saved_tracks(limit=50)
    tracks = results['items']
    totalSongs = results['total']
    songs = list()
    while results['next']:
        print('----Loaded ' + str(len(tracks)) + " / " + str(totalSongs) + '----')
        results = sp.next(results)
        tracks.extend(results['items'])
    
    for idx, item in enumerate(tracks):
        track = item['track']
        name = track['name']
        artist =  track['artists'][0]['name']

        songs.append(Song(name, artist, 0))
    #################################

    return songs

def replacePlaylistSongs(token: str, songs: List[Song]):
    sp = spotipy.Spotify(auth=token)

    # check if playlist already exists
    playlists = sp.current_user_playlists()
    current_user_info = sp.current_user()
    current_username = current_user_info['id']

    
    exists = False
    playlist_to_replace = None
    for playlist in playlists['items']:
        print(playlist['name'])
        if playlist['name'] == "50 Least Played":
            exists = True
            playlist_to_replace = playlist
            break

    # if playlist doesn't exist, make it
    if exists != True:
        playlist_to_replace = sp.user_playlist_create(user=current_username, name="50 Least Played", public=False)

    #TODO replace all the songs in the playlist with 'songs'
    sp.playlist_replace_items(playlist_to_replace)
