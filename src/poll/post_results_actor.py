from sqlalchemy.orm import Session
from src.poll.infrastructure import poll_answer_dao
from src.poll.domain.poll_answer_model import PollAnswer



def run(request: PollAnswer) -> PollAnswer:
    """
    Create answers

    :param request: All the answers from a poll
    :return: The same answers
    """
    return poll_answer_dao.create_poll_answers(poll_answer=request)
