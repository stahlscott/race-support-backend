# manage.py


import unittest

import coverage

from flask.cli import FlaskGroup

from project.server import create_app, db
from project.server.models import User, Event, Race, Rider
import subprocess
import sys

app = create_app()
cli = FlaskGroup(create_app=create_app)

# code coverage
COV = coverage.coverage(
    branch=True,
    include="project/*",
    omit=[
        "project/tests/*",
        "project/server/config.py",
        "project/server/*/__init__.py",
    ],
)
COV.start()


@cli.command()
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@cli.command()
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email="ad@min.com", password="admin", admin=True))
    db.session.commit()


@cli.command()
def create_data():
    event = Event(name="Rochester Fakelocross", bikereg_id="1", active=True)
    db.session.add(event)
    db.session.commit()
    race1 = Race(name="Cat 1 Mens", bikereg_id="2", event_id=event.id)
    race2 = Race(name="Cat 2 Mens", bikereg_id="3", event_id=event.id)
    race3 = Race(name="Cat 3 Mens", bikereg_id="4", event_id=event.id)
    race4 = Race(name="Cat 1 Womens", bikereg_id="5", event_id=event.id)
    race5 = Race(name="Cat 2 Womens", bikereg_id="6", event_id=event.id)
    race6 = Race(name="Cat 3 Womens", bikereg_id="7", event_id=event.id)
    db.session.add(race1)
    db.session.add(race2)
    db.session.add(race3)
    db.session.add(race4)
    db.session.add(race5)
    db.session.add(race6)
    db.session.commit()
    db.session.add(
        Rider(
            name="Big Guy",
            email="blah@nope.com",
            usac="123",
            bib="11",
            race_id=race1.id,
        )
    )
    db.session.add(
        Rider(
            name="Big Guy",
            email="blah@nope.com",
            usac="123",
            bib="13",
            race_id=race2.id,
        )
    )
    db.session.add(
        Rider(
            name="Another Guy",
            email="blahr@nope.com",
            usac="124",
            bib="12",
            race_id=race1.id,
        )
    )
    db.session.commit()


@cli.command()
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover("project/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover("project/tests")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage Summary:")
        COV.report()
        COV.html_report()
        COV.erase()
        sys.exit(0)
    else:
        sys.exit(1)


@cli.command()
def flake():
    """Runs flake8 on the project."""
    subprocess.run(["flake8", "project"])


if __name__ == "__main__":
    cli()
