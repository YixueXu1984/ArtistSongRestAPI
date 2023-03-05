from flask import Flask, request

app = Flask(__name__)

artists = [
    {
        "name": "Bob Dylan",
        "songs": [
            {
                "name": "Hurricane",
                "release year": 1976
            },
            {
                "name": "One more cup of coffee",
                "release year": 1976
            }
        ]
    }
]


@app.get("/artist")  # http://127.0.1:5000/artists
def get_artists():
    return {"artists": artists}


@app.post("/artist")
def create_artist():
    request_data = request.get_json()
    new_artist = {
        "name": request_data["name"],
        "songs": []
    }
    artists.append(new_artist)
    return new_artist, 201


@app.post("/artist/<string:name>/song")
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


@app.get("/artist/<string:name>")
def get_artist(name):
    for artist in artists:
        if artist["name"] == name:
            return artist
    return {"message": "Artist not found"}, 404


@app.get("/artist/<string:name>/song")
def get_songs_by_artist(name):
    for artist in artists:
        if artist["name"] == name:
            return {"songs": artist["songs"]}
    return {"message": "Artist not found"}, 404
