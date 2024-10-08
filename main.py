# Import libraries and files
from dotenv import load_dotenv
import os
from flask import Flask, session, url_for, request, redirect
from requests import post, get

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64) # allows redirect after allowing permissions

load_dotenv() # Load .env for CLIENT_ID and CLIENT_SECRET

# Variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = 'http://localhost:5000/callback'
scope = 'playlist-read-private', 'user-library-read', 'user-library-modify' # look for more scopes later

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True
)
sp = Spotify(auth_manager=sp_oauth)

@app.route("/")
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for("get_playlists"))

# callback method
@app.route("/callback")
def callback():
    sp_oauth.get_access_token(request.args["code"])
    return redirect(url_for("get_liked_songs"))

# use this later on current_user_saved_tracks() for getting liked songs and not playlists

@app.route("/get_liked_songs") # not exactly working as intended
def get_liked_songs():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    liked_songs = sp.current_user_saved_tracks()
    liked_songs_info = [(song["name"], song["external_urls"]["spotify"]) for song in liked_songs["items"]]
    liked_songs_html = "<br>".join(f"{name}: {url}" for name, url in liked_songs_info)

    return liked_songs_html

#@app.route("/get_playlists") this function will display users saved playlists, reference later
#def get_playlists():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

    playlists = sp.current_user_playlists()
    playlists_info = [(pl["name"], pl["external_urls"]["spotify"]) for pl in playlists["items"]]
    playlists_html = "<br>".join(f"{name}: {url}" for name, url in playlists_info)

    return playlists_html

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)