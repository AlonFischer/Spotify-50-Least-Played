from Music import *



def main():
    ### Spotify ###
    # Get token from spotify to make requests
    token = get_spotify_token()

    spotify_saved_songs = get_spotify_saved_songs(token)

    ### LastFM ###
    lastFM_Tracks = get_lastfm_top_tracks()

    #Add play count from lastFM_Tracks to the songs gotten from spotify
    for s in spotify_saved_songs:
        lastFMTrack = next((x for x in lastFM_Tracks if x.artist == s.artist and x.name == s.name), None)
        if lastFMTrack != None:
            s.playcount = lastFMTrack.playcount


    #sort songs by playcount in ascending order
    sorted_songs = sorted(spotify_saved_songs, key=lambda x: x.playcount, reverse=False)

    least_played_songs = sorted_songs[:50]

    # # for s in lastFM_Tracks:
    # #     if s.name == "9mm":
    # #         print(s)
    
    # # for s in spotify_saved_songs:
    # #     if s.name == "9mm":
    # #         print(s)

    # # for s in sorted_songs:
    # #     print(s)


    # print("Least played songs:")
    # for s in least_played_songs:
    #     print(s)
    
    # most_played_songs = sorted_songs[-50:]
    # print("Most played songs:")
    # for s in most_played_songs:
    #     print(s)


    ##TEST LIST###  
    # least_played_songs = [
    # Song("Song1", "Artist1", 100),
    # Song("Song2", "Artist2", 150),
    # Song("Song3", "Artist3", 120),
    # Song("Song4", "Artist4", 80),
    # ]

    #TODO Try to replace songs in playlist (make it if it doesn't exist?)
    replacePlaylistSongs(token, least_played_songs)
    ####TODO####
    #
    # create new spotify playlist containing first 50 songs
        # stretch - if playlist already exists, just modify contents instead of making new one?

#Run code
if __name__=="__main__": 
    main() 