# project/server/race/controller.py


from flask import Blueprint, jsonify

from project.server.models import Race, Rider


race_blueprint = Blueprint("race", __name__)


@race_blueprint.route("/races/<id>", methods=["GET"])
def get_race(id):
    race = Race.query.filter_by(id=id).first()
    return jsonify(race.as_dict())


@race_blueprint.route("/races", methods=["GET"])
def get_all_races():
    races = Race.query.all()
    return jsonify([race.as_dict() for race in races])


@race_blueprint.route("/races/<race_id>/riders", methods=["GET"])
def get_rider_by_race(race_id):
    riders = Rider.query.filter_by(race_id=race_id).all()
    # TODO filter this down for public consumption?
    return jsonify([rider.as_dict() for rider in riders])


@race_blueprint.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Access-Control-Allow-Headers, Content-Type, Authorization"
    return response
