from flask import Flask

app = Flask(__name__)


artists = [
    {
        "name": "Bob Dylan",
        "somgs": [
            {
                "name": "Hurricane",
                "release year": 1976
            },
            {
                "name": "One more cup of coffee",
                "release Year": 1976
            }
        ]
    }
]


@app.get("/artists") # http://127.0.0:5000/artists
def get_artists():
    return {"artists": artists}

