from flask import request, Flask, render_template
import pickle

app = Flask(__name__)

# Load the model
with open('pickle413.joblib', 'r') as pkl:    
    model = pickle.load(pkl)

genres={1: 'Movie',
    2: 'R&B',
    3: 'Dance',
    4: 'Hip-Hop',
    5: 'Pop',
    6: 'Soul',
    7: 'Indie',
    8: 'Alternative',
    9: 'Rap',
    10: 'Folk',
    11: 'Rock',
    12: 'A Capella',
    13: 'Country',
    14: 'Blues',
    15: 'Jazz',
    16: 'Reggae',
    17: 'World',
    18: 'Electronic',
    19: 'Reggaeton',
    20: 'Ska',
    21: 'Anime',
    22: 'Soundtrack',
    23: 'Classical',
    24: 'Opera'}
#for flask app
import numpy as np
import pandas as pd
import io
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy.util as util
import datetime


#set up API authonatication
SPOTIPY_CLIENT_ID = 'a2881ef09dc449bca632dc11c5142ea9'
SPOTIPY_CLIENT_SECRET = '2b969d5254f34183a5e65d2f9563b8c9'
username = 'jq42@cornell.edu'
scope = 'user-read-private user-read-email'
uri = 'http://localhost'
client_cred = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
auth_spotify = spotipy.client.Spotify(client_credentials_manager=client_cred)

categoricals = [
    'acousticness',
    'danceability',
    'duration_ms', 
    'energy',
    'instrumentalness',
    'key',
    'liveness',
    'loudness',
    'mode',
    'speechiness',
    'tempo',
    'time_signature',
    'valence'
#     ''
]


def get_requested_song_df(title):
    q = title
    result = auth_spotify.search(q)
    result_track_id = result['tracks']["items"][0]["id"]
    result_track_features =  auth_spotify.audio_features(result_track_id)
    result_track=pd.DataFrame()
    for i in categoricals:
            result_track[i] = [0]
    for i in categoricals:
            result_track[i] = result_track_features[0][i]
    result_track['explicit'] = auth_spotify.track(result_track_id)["explicit"]
    result_track['explicit'] = result_track['explicit'].map({
        True: 1,  
        False: 0,    
    })
    result_track['release_year']=auth_spotify.track(result_track_id)["album"]["release_date"][:4]
    song_name = auth_spotify.track(result_track_id)["name"]
    artist_name = auth_spotify.track(result_track_id)["album"]["name"]
    artwork = auth_spotify.track(result_track_id)["album"]["images"][0]["url"]
    actual_genre = []
    recommendations =[]
    song_id =result_track_id
    preview_url = auth_spotify.track(result_track_id)["preview_url"]
    
    return {"model_df":result_track, 
            "song_name":song_name,
            "artist_name":artist_name,
            "artwork":artwork,
            "actual_genre":actual_genre,
            "song_id":song_id,
            "preview_url":preview_url
            
            
           }
  


# helper function
def use_model(user_input_song):
    result_dictionary=get_requested_song_df(user_input_song)
    prediction=model.predict(result_dictionary["model_df"])
    # turn prediction into text
    spotify_dict={
        "user_song_genre":genres[prediction[0]],
        "song_name":result_dictionary["song_name"],
        "artist_name":result_dictionary["artist_name"],
        "artwork":result_dictionary["artwork"],
        "actual_genre":result_dictionary["actual_genre"],
        "song_id":result_dictionary["song_id"]
    }
    return spotify_dict
    
    
    


@app.route("/")
def index():
    return render_template("index.html")

  

@app.route("/handledata", methods=["POST"])

def handledata():
    
    # use helper function to get result
    song_output=use_model(request.form["input_song"])


    return render_template("index.html", song_name=song_output)

    



if __name__ == "__main__":
    app.run(debug=True)