from sqlalchemy.orm import Session
from uuid import UUID
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
    infrastructure_poll: InfrastructurePoll = session.query(InfrastructurePoll).join(InfrastructurePoll.questions).join(
        InfrastructurePollQuestion.options).filter(InfrastructurePoll.uuid == poll).first()
    return __map_to_domain(infrastructure_poll)


def __map_to_domain(infrastructure_poll: InfrastructurePoll) -> DomainPoll:
    return DomainPoll(uuid=infrastructure_poll.uuid,
                      name=infrastructure_poll.name,
                      description=infrastructure_poll.description,
                      questions=[__map_question_to_domain(question) for question in infrastructure_poll.questions])


def __map_question_to_domain(infrastructure_poll_question: InfrastructurePollQuestion) -> DomainPollQuestions:
    return DomainPollQuestions(uuid=infrastructure_poll_question.uuid,
                               poll_uuid=infrastructure_poll_question.poll_uuid,
                               topic=infrastructure_poll_question.topic,
                               description=infrastructure_poll_question.description,
                               enabled=infrastructure_poll_question.enabled,
                               options=[__map_question_options_to_domain(options) for options in infrastructure_poll_question.options])


def __map_question_options_to_domain(infrastructure_question_options: InfrastructureQuestionOptions) -> DomainPollQuestionOptions:
    return DomainPollQuestionOptions(id=infrastructure_question_options.id,
                                     question_uuid=infrastructure_question_options.question_uuid,
                                     options=infrastructure_question_options.options)
