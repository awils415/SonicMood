import os
import spotipy
from spotipy import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read")
sp = spotipy.Spotify(auth_manager=sp_oauth)

def retry_on_token_refresh(func):
    def wrapper(*args, **kwargs):
        try:
            # Call the function and attempt the request
            result = func(*args, **kwargs)
            return result
        except spotipy.SpotifyException as e:
            # Check if the error is due to an expired token
            if 'The access token expired' in str(e):
                # Attempt to refresh the token and retry the request
                print("Refreshing token and retrying the request...")
                sp_oauth = args[0]  # Assuming the SpotifyOAuth instance is the first argument
                token_info = sp_oauth.refresh_access_token(sp_oauth.get_access_token()['refresh_token'])
                sp = spotipy.Spotify(auth=token_info['access_token'])
                return func(*args, **kwargs)  # Retry the original function call
            else:
                # If it's not a token expiration issue, raise the exception
                raise e

    return wrapper

@retry_on_token_refresh
def get_cover_art(song_title, artist_name):
    try:
        # Search for the track
        results = sp.search(q=f"track:{song_title} artist:{artist_name}", type='track', limit=1)

        # Extract cover art URL
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            cover_art_url = track['album']['images'][0]['url'] if track['album']['images'] else None
            return cover_art_url
        else:
            print("Track not found.")
            return None
    except spotipy.SpotifyException as e:
        print(f"Error: {e}")
        return None