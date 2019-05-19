# project/server/api/controller.py

import json
import requests

from flask import Blueprint, jsonify, Response, request


BASE_URL = "https://www.bikereg.com/api/director"


def get_api_token():
    url = f"{BASE_URL}/PromoterLogin"
    username = "username"
    password = "password"
    resp = requests.post(url, json={"username": username, "password": password})
    resp_json = json.loads(resp.json()["PromoterLoginResult"])
    return resp_json


def get_events():
    url = f"{BASE_URL}/PromoterEvents"
    token = "TBD"
    resp = requests.post(url, json={"token": token})
    print(resp)
    resp_json = resp.json()
    return resp_json


def get_categories():
    url = f"{BASE_URL}/EventCategories"
    token = "TBD"
    resp = requests.post(url, json={"token": token})
    print(resp)
    resp_json = resp.json()
    return resp_json


def get_entries():
    url = f"{BASE_URL}/EventEntries"
    token = "TBD"
    resp = requests.post(url, json={"token": token})
    resp_json = resp.json()
    return resp_json
