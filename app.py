from flask import Flask, render_template, request
from analyzer import analyze_sentiment

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        song_title = request.form["song_title"]
        artist_name = request.form["artist_name"]
        response = analyze_sentiment(song_title, artist_name)
        
        if response:
            sentiment = response
            return render_template('result.html', song_title=song_title, artist_name=artist_name, sentiment=sentiment)
        else:
            return render_template('error.html', error_message="Error analyzing sentiment. Try again later.")


if __name__ == "__main__":
    app.run(debug=True)
