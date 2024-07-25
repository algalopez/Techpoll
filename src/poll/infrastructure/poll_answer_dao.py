from typing import List
from sqlalchemy.orm import Session
from uuid import UUID
from datetime import datetime
from src.poll.infrastructure.poll_answer_entity import PollAnswer as InfrastructurePollAnswer
from src.poll.domain.poll_answer_model import PollAnswer as DomainPollAnswer
from src.poll.domain.poll_answer_model import QuestionAnswer as DomainQuestionAnswer
from src.shared import database_connection
from sqlalchemy import func


def get_poll_answers(user: str, key: str, poll_uuid: str) -> DomainPollAnswer:
    session: Session = database_connection.get_session()
    return __find_poll_answers(session=session, user=user, key=key, poll_uuid=poll_uuid)


def create_poll_answers(poll_answer: DomainPollAnswer) -> DomainPollAnswer:
    session: Session = database_connection.get_session()
    try:
        return __create_poll_answers(session=session, poll_answer=poll_answer)
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def __find_poll_answers(session: Session, user: str, key: str, poll_uuid: str) -> DomainPollAnswer:
    print(f"key = {key}, poll = {poll_uuid}")
    subquery = session.query(
        InfrastructurePollAnswer.key,
        InfrastructurePollAnswer.poll_uuid,
        InfrastructurePollAnswer.question_uuid,
        func.max(InfrastructurePollAnswer.id).label('latest_id')
    ).group_by(
        InfrastructurePollAnswer.key,
        InfrastructurePollAnswer.poll_uuid,
        InfrastructurePollAnswer.question_uuid
    ).subquery()

    latest_answers = session.query(InfrastructurePollAnswer).join(
        subquery,
        (InfrastructurePollAnswer.key == subquery.c.key) &
        (InfrastructurePollAnswer.poll_uuid == subquery.c.poll_uuid) &
        (InfrastructurePollAnswer.question_uuid == subquery.c.question_uuid) &
        (InfrastructurePollAnswer.id == subquery.c.latest_id)
    ).filter(
        InfrastructurePollAnswer.key == key,
        InfrastructurePollAnswer.poll_uuid == poll_uuid
    ).all()

    domain_question_answers: List[DomainQuestionAnswer] = [__map_to_domain(
        infrastructurePollAnswer) for infrastructurePollAnswer in latest_answers]

    return DomainPollAnswer(user=user, key=key, datetime=None, poll_uuid=poll_uuid, answers=domain_question_answers)


def __map_to_domain(self) -> DomainQuestionAnswer:
    return DomainQuestionAnswer(question_uuid=self.question_uuid, value=self.value)


def __create_poll_answers(session: Session, poll_answer: DomainPollAnswer) -> DomainPollAnswer:
    infrastructure_poll_answers: List[InfrastructurePollAnswer] = [__map_to_infrastructure(
        user=poll_answer.user, key=poll_answer.key, datetime=poll_answer.datetime, poll_uuid=poll_answer.poll_uuid, domain_question_answer=answer) for answer in poll_answer.answers]

    session.add_all(infrastructure_poll_answers)
    session.commit()
    return poll_answer


def __map_to_infrastructure(user: str, key: str, datetime: datetime, poll_uuid: UUID, domain_question_answer: DomainQuestionAnswer) -> InfrastructurePollAnswer:
    return InfrastructurePollAnswer(user=user, key=key, datetime=datetime.strftime('%Y-%m-%d %H:%M:%S'), poll_uuid=str(poll_uuid), question_uuid=domain_question_answer.question_uuid, value=domain_question_answer.value)

