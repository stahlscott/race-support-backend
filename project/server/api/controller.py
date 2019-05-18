# project/server/api/controller.py

import json
import requests

from flask import Blueprint, jsonify, Response, request
from flask_login import login_required


api_blueprint = Blueprint("api", __name__)

BASE_URL = "https://www.bikereg.com/api/director"


@login_required
@api_blueprint.route("/api/login")
def get_api_token():
    url = f"{BASE_URL}/PromoterLogin"
    username = "username"
    password = "password"
    resp = requests.post(url, json={"username": username, "password": password})
    resp_json = json.loads(resp.json()["PromoterLoginResult"])
    if resp_json["Status"] == "1":
        return jsonify(resp_json)


@api_blueprint.route("/api/events")
@login_required
def get_events():
    url = f"{BASE_URL}/PromoterEvents"
    token = "TBD"
    resp = requests.post(url, json={"token": token})
    print(resp)
    resp_json = resp.json()
    print(resp_json)
    return jsonify(resp_json)


@api_blueprint.route("/api/categories")
@login_required
def get_categories():
    url = f"{BASE_URL}/EventCategories"
    token = "TBD"
    resp = requests.post(url, json={"token": token})
    print(resp)
    resp_json = resp.json()
    print(resp_json)
    return jsonify(resp_json)


@api_blueprint.route("/api/entries")
@login_required
def get_entries():
    url = f"{BASE_URL}/EventEntries"
    token = "TBD"
    resp = requests.post(url, json={"token": token})
    resp_json = resp.json()
    print(resp_json)
    return jsonify(resp_json)
