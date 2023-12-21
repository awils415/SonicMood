import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_sentiment(song_title, artist_name):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a witty, sarcastic person."},
                {
                    "role": "user",
                    "content": f"give a sentiment analysis of {song_title} by {artist_name} in a short phrase. don't mention the song at all just say what you think of it in a short phrase",
                },
            ],
            max_tokens=20,
        )

        return completion.choices[0].message.content

    except Exception as e:
        print(f"Error analyzing sentiment with OpenAI API: {e}")
        return None
