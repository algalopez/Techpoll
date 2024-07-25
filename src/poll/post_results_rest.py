from src.poll.domain.poll_answer_model import PollAnswer, QuestionAnswer
from flask import Blueprint, request
from src.poll import post_results_actor
from uuid import UUID
from datetime import datetime as datetimeLib
from datetime import timezone as timezoneLib
import jsonpickle
import logging

post_results_resource = Blueprint('post_results_resource', __name__)

@post_results_resource.route('/rest/poll/send-results', methods=['POST'])
def send_results():
    request_data = request.get_json()
    logging.info("request: " + str(request_data))
    poll_result: PollAnswer = map_to_poll_result(request_data)
    logging.info("poll_result: " + str(poll_result))
    return jsonpickle.encode(post_results_actor.run(poll_result), unpicklable=False)

def map_to_poll_result(request_data) -> PollAnswer: 
    user = request_data['user']
    key = request_data['key']
    datetime = datetimeLib.now(timezoneLib.utc)
    poll_uuid = UUID(request_data['poll_uuid'])
    answers = [map_to_question_answer(answer) for answer in request_data['answers']]
    return PollAnswer(user=user, key=key, datetime=datetime, poll_uuid=poll_uuid, answers=answers)

def map_to_question_answer(answer) -> QuestionAnswer:
    return QuestionAnswer(question_uuid=UUID(answer['question_uuid']), value=answer['value'])


