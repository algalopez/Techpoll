from flask import Blueprint, request
from src.poll import get_poll_actor

import jsonpickle
import logging

get_poll_resource = Blueprint('get_poll_resource', __name__)


@get_poll_resource.route('/rest/poll/get-poll', methods=['GET'])
def send_results():
    poll_uuid = request.args.get('poll')
    logging.info(f"request: {poll_uuid}")
    poll_results = get_poll_actor.run(poll_uuid)
    return jsonpickle.encode(poll_results, unpicklable=False)

