from sclib import SoundcloudAPI, Track, Playlist
#cloudlink = "https://soundcloud.com/user-300323425566/6edqtk1tlnfa"
def main(link):
    api = SoundcloudAPI()
    track = api.resolve(link)
    assert type(track) is Track
    
    artist = track.artist
    title = track.title
    return title, artist
if __name__ == "__main__":
    main(cloudlink)

