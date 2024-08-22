# Import libraries and files
from dotenv import load_dotenv
import os 
import json
import base64
from requests import post, get

load_dotenv() # Load .env for CLIENT_ID and CLIENT_SECRET

# Variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


# Main Method
def main():
    print("Welcome to Spotify Sort! To start, let's login to your Spotify account.")


main()
# Methods

def get_token(): 
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8") #encode auth string into bytes
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8") # encodes string in base 64 & convert back to utf-8

    url = "https://accounts.spotify.com/api/token" 
    headers = {     # dictionary with headers + encoded authentication string
        "Authorization": "Basic " + auth_base64, 
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"} # data to be sent in POST request
    result = post(url, headers = headers, data = data) # Send post request to url with headers and data
    json_result = json.loads(result.content) # parse json response content into python
    token = json_result["access_token"] # Extract access token from json response
    return token 

def get_auth_header(token): # Take oAuth token & return dictionary with authorization
    return {"Authorization": "Bearer " + token}