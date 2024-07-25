from typing import List
from sqlalchemy.orm import Session, aliased
from uuid import UUID
from datetime import datetime
from src.poll.infrastructure.poll_entity import Poll as InfrastructurePoll
from src.poll.infrastructure.poll_entity import PollQuestion as InfrastructurePollQuestion
from src.poll.infrastructure.poll_entity import QuestionOptions as InfrastructureQuestionOptions
from src.poll.domain.poll_model import Poll as DomainPoll
from src.poll.domain.poll_model import PollQuestions as DomainPollQuestions
from src.poll.domain.poll_model import PollQuestionOptions as DomainPollQuestionOptions
from src.shared import database_connection


def get_poll(poll_uuid: UUID) -> DomainPoll:
    session: Session = database_connection.get_session()
    try:
        return __find_poll(session=session, poll=poll_uuid)
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def __find_poll(session: Session, poll: str) -> DomainPoll:
    infrastructurePoll: InfrastructurePoll = session.query(InfrastructurePoll).join(InfrastructurePoll.questions).join(
        InfrastructurePollQuestion.options).filter(InfrastructurePoll.uuid == poll).first()
    return __map_to_domain(infrastructurePoll)


def __map_to_domain(infrastructurePoll: InfrastructurePoll) -> DomainPoll:
    return DomainPoll(uuid=infrastructurePoll.uuid,
                      name=infrastructurePoll.name,
                      description=infrastructurePoll.description,
                      questions=[__map_question_to_domain(question) for question in infrastructurePoll.questions])


def __map_question_to_domain(infrastructurePollQuestion: InfrastructurePollQuestion) -> DomainPollQuestions:
    return DomainPollQuestions(uuid=infrastructurePollQuestion.uuid,
                               poll_uuid=infrastructurePollQuestion.poll_uuid,
                               topic=infrastructurePollQuestion.topic,
                               description=infrastructurePollQuestion.description,
                               enabled=infrastructurePollQuestion.enabled,
                               options=[__map_question_options_to_domain(options) for options in infrastructurePollQuestion.options])


def __map_question_options_to_domain(infrastructureQuestionOptions: InfrastructureQuestionOptions) -> DomainPollQuestionOptions:
    return DomainPollQuestionOptions(id=infrastructureQuestionOptions.id,
                                     question_uuid=infrastructureQuestionOptions.question_uuid,
                                     options=infrastructureQuestionOptions.options)
