class Song:
    pass

    def __init__(self, name, artist, playcount, uri) -> None:
        self.artist = str(artist)
        self.name = str(name)
        self.playcount = str(playcount)
        self.uri = str(uri)

    def __str__(self):
        return f"Name: {self.name}, Artist: {self.artist}, Playcount: {self.playcount}, URI: {self.uri}"