"""
Homework #7

This code describes
my favorite song



artist = 'The Prodigy'								# British electronic dance music band
genre = 'Techno, rave'
song = 'Woodoo peoplle'
album = 'Music for the jilted generation'
released = 1994
lenghtInSeconds = 387								#lenght in minutes 6:27
"""

myFavoriteSong = {'artist' : 'The Prodigy', 'genre' : 'Techno, rave', 'song' : 'Woodoo people', 'album' : 'Music for the jilted generation', 'released' : 1994, 'lenghtInSeconds' : 387}

Key = 'song'
Value = 'Woodoo people'


print('Artist - ' + myFavoriteSong['artist'])
print('Genre - ' + myFavoriteSong['genre'])
print('Song - ' + myFavoriteSong['song'])
print('Album - ' + myFavoriteSong['album'])
print('Released - ' + str(myFavoriteSong['released']))
print('Lengh - ' + str(myFavoriteSong['lenghtInSeconds']) + ' seconds')



def rightOrWrong (Key, Value):
	if Key in myFavoriteSong:
		if Value == myFavoriteSong[Key]:
			print('You are right')
		else:
			print('You are wrong')
	else:
		print('You are wrong')


rightOrWrong(Key, Value)