'''Query Spotify API based on Artist name and Track, convert using 'audio analysis' to match comparasion dataset'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initalize spotipy
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Get user input, Artist & Track
artist = input('Enter an artist: ')
track = input('Enter a track name: ')

# Query Spotify for artist & track name, return first item
track_search= spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=1, market='US')
track_id = track_search['tracks']['items'][0]['id']

# Convert result to format for comparison with dataset
user_audio = spotify.audio_analysis(track_id)

print(user_audio)