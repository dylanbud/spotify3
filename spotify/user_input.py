'''Query Spotify API based on Artist name and Track, convert using 'audio analysis' to match comparasion dataset'''

from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

# Initalize spotipy
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def convert(artist, track):
    track_search= spotify.search(q='artist:' + artist + ' track:' + track, type='track', limit=1, market='US')
    track_id = track_search['tracks']['items'][0]['id']
    user_audio = spotify.audio_features(track_id)
    df = pd.DataFrame.from_records(user_audio)
    df.drop(columns = ['key', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'], inplace=True)
    df.to_numpy().reshape(1,-1)
    return (df)