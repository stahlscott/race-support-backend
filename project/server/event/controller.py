# project/server/event/controller.py


from flask import Blueprint, jsonify

# from flask_login import login_user, logout_user, login_required

from project.server import db
from project.server.models import Event, Race
from project.server.auth import requires_auth


event_blueprint = Blueprint("event", __name__)


@event_blueprint.route("/events/<id>", methods=["GET"])
def get_event(id):
    event = Event.query.filter_by(id=id).first()
    return jsonify(event.as_dict())


@event_blueprint.route("/events", methods=["GET"])
@requires_auth
def get_all_events():
    events = Event.query.all()
    return jsonify([event.as_dict() for event in events])


@event_blueprint.route("/events/<event_id>/races", methods=["GET"])
def get_race_by_event(event_id):
    races = Race.query.filter_by(event_id=event_id).all()
    return jsonify([race.as_dict() for race in races])


@event_blueprint.route("/events/<event_id>/active", methods=["GET"])
@requires_auth
def set_event_active(event_id):
    events = Event.query.all()
    event_id = int(event_id)
    updated_event = None
    for event in events:
        if event.id == event_id:
            event.active = True
            updated_event = event
        else:
            event.active = False
    db.session.commit()
    return jsonify(updated_event.as_dict())


@event_blueprint.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Access-Control-Allow-Headers, Content-Type, Authorization"
    return response
