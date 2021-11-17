import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle
import requests


def api(user_song_data_fetch):
    dummy_data = np.array([[ 3.88000e-01,  8.79000e-01, -6.47300e+00,  0.00000e+00,
         3.72000e-02,  2.07000e-03,  9.28000e-05,  2.95000e-01,
         5.80000e-01,  1.56434e+02]])
    return dummy_data

model = pickle.load(open('model.pkl', 'rb'))
Song_data = pd.read_csv('Song_data.csv', index_col=0)

def get_recommendation(user_song):
    user_song_data = api(user_song)
    rec_raw = model.kneighbors(user_song_data, 5, return_distance=False)
    rec_list=rec_raw.tolist()[0]
    return Song_data.iloc[rec_list]

# get_recommendation('The User Input')