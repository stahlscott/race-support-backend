# project/server/event/controller.py


from flask import Blueprint, jsonify

# from flask_login import login_user, logout_user, login_required

# from project.server import db
from project.server.models import Event, Race


event_blueprint = Blueprint("event", __name__)


@event_blueprint.route("/events/<id>", methods=["GET"])
def get_event(id):
    event = Event.query.filter_by(id=id).first()
    return jsonify(event.as_dict())


@event_blueprint.route("/events", methods=["GET"])
def get_all_events():
    events = Event.query.all()
    return jsonify([event.as_dict() for event in events])


@event_blueprint.route("/events/<event_id>/races", methods=["GET"])
def get_race_by_event(event_id):
    races = Race.query.filter_by(event_id=event_id).all()
    return jsonify([race.as_dict() for race in races])


def set_event_active(event_id):
    pass


@event_blueprint.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Access-Control-Allow-Headers, Content-Type, Authorization"
    return response
