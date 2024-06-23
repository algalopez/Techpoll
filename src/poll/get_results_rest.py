from src.poll.domain.question_answer_model import QuestionResult
from src.poll.domain.poll_answer_model import PollAnswer
from flask import Blueprint, request
from src.poll import post_results_actor
from uuid import UUID
from datetime import datetime
import jsonpickle
import logging

post_results_resource = Blueprint('post_results_resource', __name__)

@post_results_resource.route('/rest/poll/send-results', methods=['POST'])
def send_results():
    request_data = request.get_json()
    logging.info("request: " + str(request_data))
    pollResult: PollAnswer = mapToPollResult(request_data)
    logging.info("pollResult: " + str(pollResult))
    return jsonpickle.encode(post_results_actor.run(pollResult), unpicklable=False)

def mapToPollResult(request_data) -> PollAnswer: 
    user = request_data['user']
    key = request_data['key']
    datetime = datetime.now(datetime.utc)
    poll_uuid = UUID(request_data['poll_uuid'])
    answers = [mapToQuestionResult(answer) for answer in request_data['answers']]
    return PollAnswer(user=user, key=key, datetime=datetime, poll_uuid=poll_uuid, answers=answers)

def mapToQuestionResult(answer) -> QuestionResult:
    return QuestionResult(question_uuid=UUID(answer['question_uuid']), value=answer['value'])


