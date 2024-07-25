from flask import Blueprint, request
from src.poll import get_results_actor

import jsonpickle
import logging

get_results_resource = Blueprint('get_results_resource', __name__)


@get_results_resource.route('/rest/poll/get-results', methods=['GET'])
def send_results():
    poll_uuid = request.args.get('poll')
    key = request.args.get('key')
    logging.info(f"request: {poll_uuid} - {key}")
    poll_results = get_results_actor.run(poll_uuid, key)
    return jsonpickle.encode(poll_results, unpicklable=False)

