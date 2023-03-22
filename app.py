from flask import Flask, request
from flask_smorest import abort
from db import songs, albums, artists
import uuid

app = Flask(__name__)


@app.get("/artist")  # http://127.0.1:5000/artist
def get_artists():
    return {"artists": list(artists.values())}


@app.post("/artist")
def create_artist():
    artist_data = request.get_json()
    artist_id = uuid.uuid4().hex
    artist = {**artist_data, "id": artist_id}
    artists[artist_id] = artist
    return artist, 201


@app.post("/song")
def create_song():
    song_data = request.get_json()
    if song_data["artist_id"] not in artists:
        abort(404, message="Artist not found.")
    song_id = uuid.uuid4().hex
    song = {**song_data, "id": song_id}
    songs[song_id] = song

    return song, 201


@app.get("/song")
def get_all_songs():
    return {"songs": list(songs.values())}


@app.get("/artist/<string:artist_id>")
def get_artist(artist_id):
    try:
        return artists[artist_id]
    except KeyError:
        abort(404, message="Artist not found.")


@app.get("/song/<string:song_id>")
def get_song(song_id):
    try:
        return songs[song_id]
    except KeyError:
        abort(404, message="Song not found.")
