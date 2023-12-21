from flask import Flask, render_template, request
from analyzer import analyze_sentiment
from get_lyrics import get_lyrics

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        song_title = request.form["song_title"]
        artist_name = request.form["artist_name"]
        lyrics = get_lyrics(song_title, artist_name)
        
        if lyrics:
            sentiment_score = analyze_sentiment(lyrics)
            return render_template('result.html', song_title=song_title, artist_name=artist_name, sentiment_score=sentiment_score)
        else:
            return render_template('error.html', error_message="Lyrics not found.")


if __name__ == "__main__":
    app.run(debug=True)
