import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import artists

blp = Blueprint("artists", __name__, description="Operations on Artists")


@blp.route("/artist/<string:artist_id>")
class Artist(MethodView):
    def get(self, artist_id):
        # todo
        pass

    def delete(self, artist_id):
        # todo
        pass
