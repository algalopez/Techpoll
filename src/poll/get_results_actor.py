from src.poll.infrastructure import poll_answer_dao
from src.poll.domain.poll_answer_model import PollAnswer


def run(request: PollAnswer):
    """
    Get results published by a user

    :param request: A list id
    :return: The list
    """
    poll_answer_dao.create_poll_answers()
    return hello.Hello(name=request)
