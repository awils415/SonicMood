from flask import Flask, render_template, request
from analyzer import analyze_sentiment
from cover_art import get_cover_art

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if request.method == "POST":
        song_title = request.form.get("song_title")
        artist_name = request.form.get("artist_name")

        # Perform sentiment analysis
        sentiment = analyze_sentiment(song_title, artist_name)

        # Get cover art URL
        cover_art_url = get_cover_art(song_title, artist_name)

        # Render the result template with all the information
        if sentiment and cover_art_url:
            return render_template('result.html', song_title=song_title, artist_name=artist_name, sentiment=sentiment, cover_art_url=cover_art_url)
        else:
            return render_template('error.html', error_message="Error analyzing sentiment or cover art not found. Try again later.")
    else:
        return render_template('error.html', error_message="Invalid request method.")

if __name__ == "__main__":
    app.run(debug=True)
