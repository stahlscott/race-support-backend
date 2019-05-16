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
    name = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    usac = db.Column(db.Text, unique=True, nullable=False)
    bib = db.Column(db.Text, nullable=False)
    event = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    checked_in = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, email, usac, bib, event, checked_in=False):
        self.name = name
        self.email = email
        self.usac = usac
        self.bib = bib
        self.event = event
        self.created_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"<Rider {self.name}>"


class Race(db.Model):

    __tablename__ = "races"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    event = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, usac, bib, event, checked_in=False):
        self.name = name
        self.email = email
        self.usac = usac
        self.bib = bib
        self.event = event
        self.created_on = datetime.datetime.now()

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"<Race {self.name}>"
