def make_album(artist_name, album_title, number_of_songs=None):
	"""Build a dictionary describing a music album."""
	album = {'artist': artist_name, 'album': album_title}
	if number_of_songs:
		album['number of songs'] = number_of_songs
	return album


