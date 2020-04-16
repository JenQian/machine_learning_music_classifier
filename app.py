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