import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 1. Initialize the Secret Vault
load_dotenv()

# 2. Setup Authentication Logic
def get_spotify_client():
    # Define what the Aether system is allowed to do (Scopes)
    # We want to read status and change playback (volume/play/pause)
    scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
    
    auth_manager = SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope=scope,
        open_browser=True
    )
    
    return spotipy.Spotify(auth_manager=auth_manager)

# 3. Core Music Functions
def play_pause():
    sp = get_spotify_client()
    playback = sp.current_playback()
    
    if playback and playback.get('is_playing'):
        sp.pause_playback()
        print("Aether: Music Paused.")
    else:
        sp.start_playback()
        print("Aether: Music Started.")

if __name__ == "__main__":
    print("Aether: Testing Spotify Connection...")
    try:
        user_info = get_spotify_client().current_user()
        print(f"Success! Linked to account: {user_info['display_name']}")
    except Exception as e:
        print(f"Error: Could not connect to Spotify. Check your .env file. \n{e}")