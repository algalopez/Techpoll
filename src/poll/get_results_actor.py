from src.poll.domain.poll_model import Poll
from src.poll.domain.poll_answer_model import QuestionAnswer
from src.poll.infrastructure import poll_dao, poll_answer_dao
from src.poll.domain.score_model import Score
from uuid import UUID
import logging


def run(poll_uuid: UUID, key: str) -> Score:
    """
    Get score for a poll and a user

    :param poll: The poll uuid
    :param key: The user key
    :return: The list
    """
    poll: Poll = poll_dao.get_poll(poll_uuid=poll_uuid)
    question_answer = poll_answer_dao.get_poll_answers(user="", key=key, poll_uuid=poll_uuid)

    scores = list(map(lambda answer: calculate_points(answer=answer, poll=poll), question_answer.answers))
    logging.info(f"scores: {scores}")
    
    score = sum(map(lambda x: x if x is not None else 0, scores))
    return Score(value=score)


def calculate_points(answer: QuestionAnswer, poll: Poll) -> int:
    matching_question = next(
        (question for question in poll.questions if question.uuid == answer.question_uuid),
        None
    )
    
    if matching_question is None:
        print("no matching question")
        return 0

    matching_option = next(
        (option for question_option in matching_question.options for option in question_option.options
         if option["name"] == answer.value),
        None
    )
    
    if matching_option is None:
        print("no matching option")
        return 0

    return matching_option["value"]