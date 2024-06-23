from dataclasses import dataclass
from typing import List

from sqlalchemy import Column, Unicode, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.poll.domain.question_answer_model import QuestionAnswer as ModelQuestionAnswer
from src.shared.database_connection import BASE

@dataclass
class PollAnswer(BASE):
    __tablename__ = "poll_answer"
    id: int = Column(Integer, primary_key=True)
    user: str = Column(Unicode)
    key: str = Column(Unicode)
    datetime: str = Column(DateTime)
    poll_uuid: str = Column(Unicode)
    question_uuid: str = Column(Unicode)
    value: str = Column(Unicode)

