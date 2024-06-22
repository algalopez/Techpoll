from src.poll.question_result_model import QuestionResult
from src.poll.poll_result_model import PollResult
from flask import Blueprint, request
from src.poll import post_results_actor
from uuid import UUID
import jsonpickle
import logging

post_results_resource = Blueprint('post_results_resource', __name__)

@post_results_resource.route('/rest/poll/send-results', methods=['POST'])
def send_results():
    request_data = request.get_json()
    logging.info("request: " + str(request_data))
    pollResult: PollResult = mapToPollResult(request_data)
    logging.info("pollResult: " + str(pollResult))
    return jsonpickle.encode(post_results_actor.run(pollResult), unpicklable=False)

def mapToPollResult(request_data) -> PollResult: 
    poll_uuid = UUID(request_data['poll_uuid'])
    answers = [mapToQuestionResult(answer) for answer in request_data['answers']]
    return PollResult(poll_uuid=poll_uuid, answers=answers)

def mapToQuestionResult(answer) -> QuestionResult:
    return QuestionResult(question_uuid=UUID(answer['question_uuid']), value=answer['value'])


