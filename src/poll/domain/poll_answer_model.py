from src.poll.domain.question_answer_model import QuestionAnswer
from dataclasses import dataclass, field
from uuid import UUID
from typing import List
from datetime import datetime

@dataclass
class PollAnswer:
    user: str
    key: str
    datetime: datetime
    poll_uuid: UUID
    answers: List[QuestionAnswer] = field(default_factory=list)
