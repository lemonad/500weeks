from flask import request
from flask_restful import Resource
from Model import db, User as User, UserSchema

user_schema_many = UserSchema(many=True)
user_schema = UserSchema()


class UserResource(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first_or_404()
        return (
            {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            200,
        )

    def put(self, username):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(username=data["username"]).first()
        if not user:
            return {"message": "User does not exist"}, 400
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        db.session.commit()

        result = user_schema.dump(user).data
        return {"status": "success", "data": result}, 204

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        users = user_schema_many.dump(users).data
        return {'status': 'success', 'data': users}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {"message": "No input data provided"}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(username=data["username"]).first()
        if user:
            return {"message": "User already exists"}, 400
        user = User(
            username=json_data["username"],
            first_name=json_data["first_name"],
            last_name=json_data["last_name"],
            email=json_data["email"],
        )
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user).data
        return {"status": "success", "data": result}, 201
