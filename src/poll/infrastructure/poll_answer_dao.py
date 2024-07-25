from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from src.poll.infrastructure.poll_answer_entity import PollAnswer as InfrastructurePollAnswer
from src.poll.domain.poll_answer_model import PollAnswer as DomainPollAnswer
from src.poll.domain.poll_answer_model import QuestionAnswer as DomainQuestionAnswer
from src.shared import database_connection


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


    logging.info('Getting all lists')
    session: Session = database_connection.get_session()
    try:
        domain_lists: List[ModelList] = [repository_list.map_to_domain() for repository_list in
                                         list_dao.get_lists(session)]
        logging.debug('lists: %s' % domain_lists)
    finally:
        session.close()
    return domain_lists
"""

def create_poll_answers(pollAnswer: DomainPollAnswer) -> DomainPollAnswer:
    session: Session = database_connection.get_session()
    try:
        return __create_poll_answers(session=session, pollAnswer=pollAnswer)
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_poll_answers(session: Session, user: str, key: str, poll: str) -> DomainPollAnswer:
    infrastructurePollAnswers: List[InfrastructurePollAnswer] = session.query(
        InfrastructurePollAnswer).filter(InfrastructurePollAnswer.question_uuid == poll).all()

    domainQuestionAnswers: List[DomainQuestionAnswer] = [__map_to_domain(
        infrastructurePollAnswer) for infrastructurePollAnswer in infrastructurePollAnswers]

    return DomainPollAnswer(user=user, key=key, poll=poll, answers=domainQuestionAnswers)



def __create_poll_answers(session: Session, pollAnswer: DomainPollAnswer) -> DomainPollAnswer:
    infrastructurePollAnswers: List[InfrastructurePollAnswer] = [__map_to_infrastructure(
        user=pollAnswer.user, key=pollAnswer.key, datetime=pollAnswer.datetime, poll_uuid=pollAnswer.poll_uuid, domainQuestionAnswer=answer) for answer in pollAnswer.answers]

    session.add_all(infrastructurePollAnswers)
    session.commit()
    return pollAnswer


def __map_to_domain(self) -> DomainQuestionAnswer:
    return DomainQuestionAnswer(question_uuid=self.question_uuid, value=self.value)


def __map_to_infrastructure(user: str, key: str, datetime: datetime, poll_uuid: UUID, domainQuestionAnswer: DomainQuestionAnswer) -> InfrastructurePollAnswer:
    return InfrastructurePollAnswer(user=user, key=key, datetime=datetime.strftime('%Y-%m-%d %H:%M:%S'), poll_uuid=str(poll_uuid), question_uuid=domainQuestionAnswer.question_uuid, value=domainQuestionAnswer.value)

