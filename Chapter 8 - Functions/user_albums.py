def make_album(artist_name, album_title, number_of_songs=None):
	"""Build a dictionary describing a music album."""
	album = {'artist': artist_name, 'album': album_title}
	if number_of_songs:
		album['number of songs'] = number_of_songs
	return album

# Create limitless, user-generated dictionaries. 
while True:
	print("---Album Builder---\n(enter 'q' to quit)")
	artist = input("Enter the musical artist: ")
	if artist == 'q':
		break
	album = input("Enter the title of the album: ")
	if album == 'q':
		break
	new_album = make_album(artist, album)
	print(new_album)

