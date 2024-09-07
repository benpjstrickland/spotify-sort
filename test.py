from dotenv import load_dotenv
import os
from flask import Flask, session, url_for, request, redirect
from requests import post, get

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64) # allows redirect after allowing permissions