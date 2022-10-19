# Ben Siri 10-2-22
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, request

app = Flask(__name__)

scope = "user-read-recently-played"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID,
#                                                client_secret= cred.client_SECRET,
#                                                redirect_uri=cred.redirect_url,
#                                                scope=scope))

@app.route('/')
def getAuthTkn():
    artist = request.args.get('artist')
    print(artist)

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    results = sp.search(q=f"artist:{artist}")
    tracks = results['tracks']['items']

    out = ''
    for track in tracks:
        out = out + "\n" + track['name']
    return(out[1:])


@app.route('/callback')
def index():
    return("Hello World")
    # results = sp.current_user_recently_played()
    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     out = out + (idx, track['artists'][0]['name'], " - ", track['name'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

