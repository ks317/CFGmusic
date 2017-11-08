import spotipy
import spotipy.util as util

t = util.prompt_for_user_token(
	'naomi.forde@rocketmail.com','playlist-modify-public',
	client_id='98b118aeb98848beb7ca39e63a2aa6f5',
	client_secret='4d4d44ee5f30468391dd947007adc0c9',
	redirect_uri='http://localhost:8888/callback')


spotify = spotipy.Spotify(auth=t)
results = spotify.search(q='artist:' + 'The Weeknd', type='artist')

band = results['artists']['items'][0]

print band['name']
print band['popularity']