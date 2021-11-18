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
model = pickle.load(open('spotify/model.pkl', 'rb'))
Song_data = pd.read_csv('spotify/Song_data.csv', index_col=0)


def convert(artist, track):
    track_search = spotify.search(
        q='artist:' + artist + ' track:' + track, type='track', limit=1, market='US')
    if track_search['tracks']['total'] == 0:
        df = pd.DataFrame(data={'danceability': [3]})
        return df
    else:
        track_id = track_search['tracks']['items'][0]['id']
        user_audio = spotify.audio_features(track_id)
        df = pd.DataFrame.from_records(user_audio)
        df.drop(columns=['key', 'type', 'id', 'uri', 'track_href',
                'analysis_url', 'duration_ms', 'time_signature'], inplace=True)
        df.to_numpy().reshape(1, -1)
    return (df)


def get_recommendation(artist, track):
    user_song_data = convert(artist, track)
    if user_song_data.iloc[0][0] > 1:
        Song_data_error = pd.DataFrame(data={'Error finding song': ['Please use a different song']})
        return Song_data_error
    else:
        rec_raw = model.kneighbors(user_song_data, 5, return_distance=False)
        rec_list = rec_raw.tolist()[0]
        return Song_data.iloc[rec_list]
