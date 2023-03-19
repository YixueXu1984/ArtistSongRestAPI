from flask import Flask, request
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
    artist = {**artist_data, "id":artist_id}
    artists[artist_id] = artist
    return artist, 201


@app.post("/song")
def create_song(name):
    request_data = request.get_json()
    for artist in artists:
        if artist["name"] == name:
            new_song = {
                "name": request_data["name"],
                "release year": request_data["release year"]
            }
            artist["songs"].append(new_song)
            return new_song, 201

    return {"message": "Artist not found"}, 404


@app.get("/artist/<string:artist_id>")
def get_artist(artist_id):
    try:
        return artists[artist_id]
    except KeyError:
        return {"message": "Store not found"}, 404



@app.get("/artist/<string:name>/song")
def get_songs_by_artist(name):
    for artist in artists:
        if artist["name"] == name:
            return {"songs": artist["songs"]}
    return {"message": "Artist not found"}, 404
