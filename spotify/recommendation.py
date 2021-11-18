import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle
import requests
from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initalize spotipy
spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials())
model = pickle.load(open('model.pkl', 'rb'))
Song_data = pd.read_csv('Song_data.csv', index_col=0)


def convert(artist, track):
    track_search = spotify.search(
        q='artist:' + artist + ' track:' + track, type='track', limit=1, market='US')
    track_id = track_search['tracks']['items'][0]['id']
    user_audio = spotify.audio_features(track_id)
    df = pd.DataFrame.from_records(user_audio)
    df.drop(columns=['key', 'type', 'id', 'uri', 'track_href',
            'analysis_url', 'duration_ms', 'time_signature'], inplace=True)
    df.to_numpy().reshape(1, -1)
    return (df)


def get_recommendation(user_song, user_artist_name):
    user_song_data = convert(user_song, user_artist_name)
    rec_raw = model.kneighbors(user_song_data, 5, return_distance=False)
    rec_list = rec_raw.tolist()[0]
    return Song_data.iloc[rec_list]
