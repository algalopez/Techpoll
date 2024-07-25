from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Unicode, Integer, String, DateTime, JSON, UUID, TEXT, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.shared.database_connection import BASE

@dataclass
class Poll(BASE):
    __tablename__ = "poll"
    uuid = Column(Unicode, primary_key=True)
    name = Column(Unicode, nullable=False, unique=True)
    description = Column(Unicode)
    questions = relationship('PollQuestion', backref='poll', lazy=False)
    def __repr__(self):
        return (f"InfrastructurePoll(uuid='{self.uuid}', name='{self.name}', "
                f"description='{self.description}', questions='{self.questions}'")


@dataclass
class PollQuestion(BASE):
    __tablename__ = 'poll_question'
    uuid = Column(Unicode, primary_key=True)
    poll_uuid = Column(Unicode, ForeignKey('poll.uuid'), nullable=False)
    topic = Column(Unicode, nullable=False)
    description = Column(Unicode, nullable=False)
    enabled = Column(Boolean, default=True)
    options = relationship('QuestionOptions', backref='question', lazy=False)
    def __repr__(self):
        return (f"InfrastructurePollQuestion(uuid='{self.uuid}', poll_uuid='{self.poll_uuid}', "
                f"topic='{self.topic}', description='{self.description}', "
                f"enabled={self.enabled}, options={self.options}")

@dataclass
class QuestionOptions(BASE):
    __tablename__ = 'question_options'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    question_uuid: str = Column(Unicode, ForeignKey('poll_question.uuid'), nullable=False)
    options = Column(JSON, nullable=False)
    def __repr__(self):
        return (f"InfrastructureQuestionOptions(id='{self.id}', question_uuid='{self.question_uuid}', "
                f"options={self.options}")

