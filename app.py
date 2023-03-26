from flask import Flask, request
from flask_smorest import abort
from db import songs, artists
import uuid

app = Flask(__name__)


@app.get("/artist")  # http://127.0.1:5000/artist
def get_artists():
    return {"artists": list(artists.values())}


@app.get("/artist/<string:artist_id>")
def get_artist(artist_id):
    try:
        return artists[artist_id]
    except KeyError:
        abort(404, message="Artist not found.")


@app.post("/artist")
def create_artist():
    artist_data = request.get_json()
    if "name" not in artist_data:
        abort(
            400, message="Bad request. Ensure 'name' is included in the JSON payload."
        )
    for artist in artists.values():
        if artist_data["name"] == artist["name"]:
            abort(400, message=f"Artist already exists.")
    artist_id = uuid.uuid4().hex
    artist = {**artist_data, "id": artist_id}
    artists[artist_id] = artist
    return artist, 201


@app.delete("/artist/<string:artist_id>")
def delete_artist(artist_id):
    try:
        del artists[artist_id]
        return {"message": "Artist deleted."}
    except KeyError:
        abort(404, message="Artist not found.")


@app.get("/song")
def get_all_songs():
    return {"songs": list(songs.values())}


@app.get("/song/<string:song_id>")
def get_song(song_id):
    try:
        return songs[song_id]
    except KeyError:
        abort(404, message="Song not found.")


@app.post("/song")
def create_song():
    song_data = request.get_json()
    if (
            "release_year" not in song_data
            or "artist_id" not in song_data
            or "name" not in song_data
    ):
        abort(
            400,
            message="Bad request. Ensure 'release_year', 'artist_id', and 'name' are included in JSON payload."
        )
    for song in songs.values():
        if (
                song_data["name"] == song["name"]
                and song_data["artist_id"] == song["artist_id"]
        ):
            abort(400, message=f"Song already exists.")
    if song_data["artist_id"] not in artists:
        abort(404, message="Artist not found.")
    song_id = uuid.uuid4().hex
    song = {**song_data, "id": song_id}
    songs[song_id] = song

    return song, 201


@app.delete("/song/<string:song_id>")
def delete_song(song_id):
    try:
        del songs[song_id]
        return {"message": "Song deleted."}
    except KeyError:
        abort(404, message="Song not found.")


@app.put("/song/<string:song_id>")
def update_song(song_id):
    song_data = request.get_json()
    if "release_year" not in song_data or "name" not in song_data:
        abort(400, message="Bad request. Ensure'release_year and 'name' are included in the JSON payload.")

    try:
        song = songs[song_id]
        song |= song_data
        return song
    except KeyError:
        abort(404, message="Song not found.")
