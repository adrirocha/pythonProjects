import requests as r
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# USER_AGENT = os.getenv("USER_AGENT")


#-----------------------------------------------------------------------------------------------------------------------------------
input_date = input("Type the date in this format YYYY-MM-DD:")

# !! The code below is commented because Billboard limited the web scraping !!
#header = {
#    "User-Agent" : USER_AGENT
#}
#
# response = r.get(f"https://www.billboard.com/charts/hot-100/{input_date}/", headers=header)
# response.raise_for_status()
# contents = response.text

# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# !! Below I am recreating the list because Billboard has limited the web scraping. !!
song_names = ["Billie Jean", "Thriller", "Beat It"]

#-----------------------------------------------------------------------------------------------------------------------------------
sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scope="playlist-modify-private",
    redirect_uri="https://example.com"
))

try:
    # Try to get the current user's id. Here the browser should open.
    user_id = sp.current_user()["id"]
    print(f"Autenticado com sucesso! ID do usuário: {user_id}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

sp_song_uris = [sp.search(q=f"track: {song_name}", limit=1, type="track")["tracks"]['items'][0]['uri'] for song_name in song_names]

playlist_data= sp.user_playlist_create(
    user=user_id,
    name=f"{input_date} Billboard 100",
    public=False
)

sp.playlist_add_items(
    playlist_id=playlist_data['id'],
    items=sp_song_uris,
)
