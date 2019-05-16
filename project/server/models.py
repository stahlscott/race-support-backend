# project/server/models.py


import datetime

from flask import current_app

from project.server import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode("utf-8")
        self.created_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "<User {0}>".format(self.email)


class Rider(db.Model):

    __tablename__ = "riders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    usac = db.Column(db.Text, nullable=False)
    bib = db.Column(db.Text, nullable=False)
    checked_in = db.Column(db.Boolean, nullable=False, default=False)
    created_on = db.Column(db.DateTime, nullable=False)
    race_id = db.Column(db.ForeignKey("races.id"))

    def __init__(self, name, email, usac, bib, race_id, checked_in=False):
        self.name = name
        self.email = email
        self.usac = usac
        self.bib = bib
        self.created_on = datetime.datetime.now()
        self.race_id = race_id

    def get_id(self):
        return self.id

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "usac": self.usac,
            "bib": self.bib,
            "checked_in": self.checked_in,
            "race_id": self.race_id,
        }

    def __repr__(self):
        return f"<Rider {self.name}>"


class Race(db.Model):

    __tablename__ = "races"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    bikereg_id = db.Column(db.Text, unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    event_id = db.Column(db.ForeignKey("events.id"))

    def __init__(self, name, bikereg_id, event_id):
        self.name = name
        self.bikereg_id = bikereg_id
        self.created_on = datetime.datetime.now()
        self.event_id = event_id

    def get_id(self):
        return self.id

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bikereg_id": self.bikereg_id,
            "event_id": self.event_id,
        }

    def __repr__(self):
        return f"<Race {self.name}>"


class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    bikereg_id = db.Column(db.Text, unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, bikereg_id, active):
        self.name = name
        self.bikereg_id = bikereg_id
        self.active = active
        self.created_on = datetime.datetime.now()

    def is_active(self):
        return self.active

    def get_id(self):
        return self.id

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "bikereg_id": self.bikereg_id,
            "active": self.active,
        }

    def __repr__(self):
        return f"<Race {self.name}>"
