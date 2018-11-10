from flask import request
from flask_restful import Resource
from Model import db, User as UserModel

user_schema = UserModel


class User(Resource):
    def get(self, username):
        user = UserModel.query.filter_by(username=username).first_or_404()
        return {'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name}, 200
