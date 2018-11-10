from flask import request
from flask_restful import Resource
from Model import db, Goal, GoalSchema

goal_schema = GoalSchema(many=True)


class GoalResource(Resource):
    def get(self, goal_id):
        goal = Goal.query.filter_by(id=goal_id).first_or_404()
        return {'title': goal.title,
                'subtitle': goal.subtitle,
                'description': goal.description,
                'color': goal.color,
                'image_url': goal.image_url}, 200

class GoalListResource(Resource):
    def get(self):
        goals = Goal.query.all()
        goals = goal_schema.dump(goals).data
        return {'status': 'success', 'data': goals}, 200
