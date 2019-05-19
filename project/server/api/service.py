# project/server/api/controller.py

import json
import requests
import os

from flask import Blueprint, jsonify, Response, request

from project.server import db
from project.server.models import ApiToken


BASE_URL = "https://www.bikereg.com/api/director"

api_blueprint = Blueprint("api", __name__)


def get_api_token():
    url = f"{BASE_URL}/PromoterLogin"
    username = os.environ.get("API_USERNAME")
    password = os.environ.get("API_PASSWORD")
    resp = requests.post(url, json={"username": username, "password": password})
    resp_json = json.loads(resp.json()["PromoterLoginResult"])
    print(resp_json)
    if resp_json["Status"] == "1":
        apiToken = ApiToken(
            token=resp_json["authToken"], promoter_id=resp_json["promoterID"]
        )
        db.session.add(apiToken)
        db.session.commit()
        return apiToken


@api_blueprint.route("/api/events")
def get_events():
    url = f"{BASE_URL}/PromoterEvents"
    token = get_active_token()
    resp = requests.post(url, json={"token": token})
    resp_json = resp.json()
    print(resp_json)
    return Response()


@api_blueprint.route("/api/cats")
def get_categories():
    url = f"{BASE_URL}/EventCategories"
    token = get_active_token()
    resp = requests.post(url, json={"token": token})
    resp_json = resp.json()
    print(resp_json)
    return Response()


@api_blueprint.route("/api/entries")
def get_entries():
    url = f"{BASE_URL}/EventEntries"
    token = get_active_token()
    resp = requests.post(url, json={"token": token})
    resp_json = resp.json()
    print(resp_json)
    return Response()


def get_active_token():
    token = db.session.query(ApiToken).order_by(ApiToken.id.desc()).first()
    if token is None or token.is_expired():
        print("fetching new...")
        token = get_api_token()
    print(token.token)
    return token.token
