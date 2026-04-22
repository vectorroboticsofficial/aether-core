import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

class AetherMusic:
    def __init__(self):
        scope = "user-modify-playback-state user-read-playback-state"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv('SPOTIPY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
            redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
            scope=scope
        ))

    def play(self):
        try:
            self.sp.start_playback()
            print("Aether: Playback started.")
        except Exception as e:
            print(f"Aether Error: {e}")

    def pause(self):
        try:
            self.sp.pause_playback()
            print("Aether: Playback paused.")
        except Exception as e:
            print(f"Aether Error: {e}")

    def next_track(self):
        self.sp.next_track()
        print("Aether: Skipping forward.")

    def prev_track(self):
        self.sp.previous_track()
        print("Aether: Skipping back.")

    def set_volume(self, percent):
        # percent should be 0-100
        self.sp.volume(percent)
        print(f"Aether: Volume set to {percent}%")

# Initialize the controller
music = AetherMusic()