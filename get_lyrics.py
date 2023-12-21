import requests
import os

from dotenv import load_dotenv

load_dotenv()

GENIUS_API_TOKEN = os.getenv("GENIUS_API_TOKEN")


def get_lyrics(song_title, artist_name):
    headers = {"Authorization": "Bearer " + GENIUS_API_TOKEN}
    search_url = "https://api.genius.com/search"
    params = {"q": f"{song_title} {artist_name}"}

    try:
        response = requests.get(search_url, params=params, headers=headers)
        data = response.json()

        # taking first result
        hit = data["response"]["hits"][0]["result"]

        lyrics_url = hit["url"]

        lyrics_response = requests.get(lyrics_url)
        lyrics_text = lyrics_response.text

        return lyrics_text

    except Exception as e:
        return f"Error fetching lyrics: {e}"
