# project/server/rider/views.py


from flask import Blueprint, jsonify, Response, request

# from flask_login import login_user, logout_user, login_required

from project.server import db
from project.server.models import Rider


rider_blueprint = Blueprint("rider", __name__)


@rider_blueprint.route("/riders/<id>", methods=["GET"])
def get_rider(id):
    rider = Rider.query.filter_by(id=id).first()
    return jsonify(rider.as_dict())


@rider_blueprint.route("/riders", methods=["GET"])
def get_all_riders():
    riders = Rider.query.all()
    # TODO need to populate with race name
    return jsonify([rider.as_dict() for rider in riders])


@rider_blueprint.route("/riders", methods=["POST"])
def create_rider():
    if request.headers["Content-Type"] == "application/json":
        req = request.get_json()
        if req:
            rider = Rider(
                name=req.get("name"),
                email=req.get("email"),
                usac=req.get("usac"),
                bib=req.get("bib"),
                checked_in=req.get("checkedIn", False),
                race_id=req.get("raceId"),
            )
            db.session.add(rider)
            db.session.commit()
        return get_rider(rider.id)
    else:
        return Response("Requires Content-Type application/json", status=400)


@rider_blueprint.route("/riders/<id>", methods=["POST"])
def update_rider(id):
    if request.headers["Content-Type"] == "application/json":
        req = request.get_json()
        if req:
            rider = Rider.query.filter_by(id=id).first()
            rider.name = req.get("name", rider.name)
            rider.email = req.get("email", rider.email)
            rider.usac = req.get("usac", rider.usac)
            rider.bib = req.get("bib", rider.bib)
            rider.checked_in = req.get("checkedIn", rider.checked_in)
            rider.race_id = req.get("raceId", rider.race_id)
            db.session.commit()
        return jsonify(rider.as_dict())
    else:
        return Response("Requires Content-Type application/json", status=400)


@rider_blueprint.after_request
def after_request(response):
    header = response.headers
    header["Access-Control-Allow-Origin"] = "*"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Access-Control-Allow-Headers, Content-Type, Authorization"
    return response
