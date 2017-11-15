import requests

endpoint = 'https://api.spotify.com/v1/me/top/artist'

import spotipy
import spotipy.util as util

t = util.prompt_for_user_token(
	'naomi.forde@rocketmail.com','playlist-modify-public',
	client_id='98b118aeb98848beb7ca39e63a2aa6f5',
	client_secret='4d4d44ee5f30468391dd947007adc0c9',
	redirect_uri='http://localhost:8888/callback')

spotify = spotipy.Spotify(auth=t)

import pprint
import sys

import spotipy
import spotipy.util as util

try:
    import json
except ImportError:
    import simplejson as json

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    ranges = ['short_term', 'medium_term', 'long_term']
    for range in ranges:
        print "range:", range
        results = sp.current_user_top_artists(time_range=range, limit=50)
        for i, item in enumerate(results['items']):
            print i, item['name']
        print
else:
    print("Can't get token for", username)