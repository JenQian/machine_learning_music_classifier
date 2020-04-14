from flask import request, Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

  

@app.route("/handledata", methods=["POST"])
def handledata():
    print(request.form["input_song"])

    return render_template("index.html", song_name=request.form["input_song"])



if __name__ == "__main__":
    app.run(debug=True)