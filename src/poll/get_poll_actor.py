from src.poll.domain.poll_model import Poll
from src.poll.domain.poll_answer_model import QuestionAnswer
from src.poll.infrastructure import poll_dao, poll_answer_dao
from src.poll.domain.score_model import Score
from uuid import UUID
import logging


def run(poll_uuid: UUID) -> Score:
    """
    Get a poll

    :param poll: The poll uuid
    :return: The list
    """
    poll: Poll = poll_dao.get_poll(poll_uuid=poll_uuid)
    poll = override_option_values_to_none(poll)
    return poll


def override_option_values_to_none(poll: Poll) -> Poll:
    for question in poll.questions:
        for option in question.options:
            option.value = None
    return poll