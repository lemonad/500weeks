from flask import request
from flask_restful import Resource
from Model import db, Goal as GoalModel

goal_schema = GoalModel


class Goal(Resource):
    def get(self, goal_id):
        goal = GoalModel.query.filter_by(id=goal_id).first_or_404()
        return {'title': goal.title,
                'subtitle': goal.subtitle,
                'description': goal.description,
                'color': goal.color,
                'image_url': goal.image_url}, 200
