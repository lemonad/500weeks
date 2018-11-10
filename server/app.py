from flask import Blueprint
from flask_restful import Api
from resources.User import User
from resources.Goal import Goal

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(User, '/User', '/User/<string:username>')
api.add_resource(Goal, '/Goal', '/Goal/<string:goal_id>')
