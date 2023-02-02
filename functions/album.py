def make_album(title, artist, tracks=None):
    """Build a dictionary containing info about an album"""

    album_dir = {'artist': artist.title(),
                 'title': title.title(),
                 }
    if tracks:
        album_dir['tracks'] = tracks

    return album_dir

# Preparing the prompts
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(title, artist)
    print(album)





# album = make_album('eminem', 'slim shady')
# print(album)

# album = make_album('2pac', 'dirty')
# print(album)

# album = make_album('snoop dogg', 'weed')
# print(album)

# album = make_album('dr.dre', 'the next episode', 5)
# print(album)
 
  




