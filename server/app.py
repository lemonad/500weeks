from flask import Blueprint
from flask_restful import Api
from resources.Goal import GoalListResource, GoalResource
from resources.Challenge import ChallengeListResource, ChallengeResource
from resources.User import UserListResource, UserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ChallengeListResource, '/Challenge')
api.add_resource(ChallengeResource, '/Challenge/<string:challenge_id>')
api.add_resource(GoalListResource, '/Goal')
api.add_resource(GoalResource, '/Goal/<string:goal_id>')
api.add_resource(UserListResource, '/User')
api.add_resource(UserResource, '/User/<string:username>')
