from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    first_name = db.Column(db.String(64), unique=False, nullable=False)
    last_name = db.Column(db.String(64), unique=False, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, username, first_name, last_name, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    first_name = fields.String(required=False)
    last_name = fields.String(required=False)
    email = fields.String(required=True)
    # creation_date = fields.DateTime()

class Goal(db.Model):
    __tablename__ = 'goal'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=False, nullable=False)
    subtitle = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    image_url = db.Column(db.String(256), nullable=True)

    def __init__(self, title, subtitle, description, color, image_url):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.color = color
        self.image_url = image_url

class GoalSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    subtitle = fields.String(required=True)
    description = fields.String(required=False)
    color = fields.String(required=True)
    image_url = fields.String(required=True)
    # creation_date = fields.DateTime()

class Challenge(db.Model):
    __tablename__ = 'challenge'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    subtitle = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    image_url = db.Column(db.String(256), nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.id', ondelete='CASCADE'), nullable=False)
    goal = db.relationship('Goal', backref=db.backref('challenges', lazy='dynamic'))

    def __init__(self, goal_id, title, subtitle, description, image_url):
        self.goal_id = goal_id
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.image_url = image_url

class ChallengeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    subtitle = fields.String(required=True)
    description = fields.String(required=False)
    image_url = fields.String(required=True)
    goal_id = fields.Integer(required=True)

class WeekChallenge(db.Model):
    __tablename__ = "week_challenge"

    id = db.Column(db.Integer, primary_key=True)
    week_no = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy='dynamic'))
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id', ondelete='CASCADE'), nullable=False)
    challenge = db.relationship('User', backref=db.backref('challenges', lazy='dynamic'))

    def __init__(self, week_no, user_id, challenge_id):
        self.week_no = week_no
        self.user_id = user_id
        self.challenge_id = challenge_id

    def __repr__(self):
        return '{}-{}-{}-{}'.format(self.user_id, self.challenge_id)
