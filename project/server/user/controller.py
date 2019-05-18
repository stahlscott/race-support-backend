# project/server/user/controller.py


from flask import Blueprint, request, jsonify, Response
from flask_login import login_user, logout_user, login_required

from project.server import bcrypt
from project.server.models import User


user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/login", methods=["POST"])
def login():
    if request.headers["Content-Type"] == "application/json":
        req = request.get_json()
        user = User.query.filter_by(email=req.get("email")).first()
        if user and bcrypt.check_password_hash(user.password, req.get("password")):
            login_user(user)
            return jsonify({"user": user.email, "login": "success"})
        else:
            return Response("error", 401)


@user_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"logout": "success"})


@user_blueprint.route("/login/test")
@login_required
def test():
    return jsonify({"login": "success"})


@login_required
def get_bikereg_token():
    pass
