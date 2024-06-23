from sqlalchemy.orm import Session
from src.poll.infrastructure import poll_answer_dao
from src.poll.domain.poll_answer_model import PollAnswer



def run(request: PollAnswer) -> PollAnswer:
    """
    Create answers

    :param request: All the answers from a poll
    :return: The same answers
    """
    return poll_answer_dao.create_poll_answers(pollAnswer=request)





"""

    logging.info('Creating new list')
    session: Session = database_connection.get_session()
    try:
        repository_list: RepositoryList = map_to_repository(request)
        domain_list: ModelList = list_dao.create_list(session, repository_list).map_to_domain()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
    return domain_list
"""