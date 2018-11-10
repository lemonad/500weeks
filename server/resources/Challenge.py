from flask import request
from flask_restful import Resource
from Model import db, Challenge, ChallengeSchema

challenge_schema_many = ChallengeSchema(many=True)
challenge_schema = ChallengeSchema()


class ChallengeResource(Resource):
    def get(self, challenge_id):
        challenge = Challenge.query.filter_by(id=challenge_id).first_or_404()
        return {'title': challenge.title,
                'subtitle': challenge.subtitle,
                'description': challenge.description,
                'image_url': challenge.image_url,
                'goal_id': challenge.goal_id}, 200

class ChallengeListResource(Resource):
    def get(self):
        challenges = Challenge.query.all()
        challenges = challenge_schema_many.dump(challenges).data
        return {'status': 'success', 'data': challenges}, 200
