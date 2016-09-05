from flask import Blueprint, Response, request
import json


api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def info():
    return create_response({'message': 'this is the API route'})


@api.route('/email', methods=['POST'])
def send_email():
    from snakeeyes.blueprints.api.tasks import deliver_email  # because of circular dependencies

    deliver_email.delay(request.get_json())

    return create_response({'message': 'email task was registered'})


@api.route('/add', methods=['POST'])
def add():
    from snakeeyes.blueprints.api.tasks import add  # because of circular dependencies

    payload = request.get_json()
    add.delay(payload.get('first'), payload.get('second'))

    return create_response({'message': 'add task was registered'})


def create_response(content, status_code=200):
    return Response(response=json.dumps(content),
                    status=status_code,
                    mimetype="application/json")
