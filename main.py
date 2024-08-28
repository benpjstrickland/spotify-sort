# Import libraries and files
from dotenv import load_dotenv
import os
from requests import post, get
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv() # Load .env for CLIENT_ID and CLIENT_SECRET

# Variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Main Method
def main():
    print("Welcome to Spotify Sort! To start, let's login to your Spotify account.")
    print(client_id, client_secret) # testing

main()