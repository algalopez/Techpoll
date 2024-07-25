from dataclasses import dataclass, field
from uuid import UUID
from typing import List
from datetime import datetime

@dataclass
class QuestionAnswer:
    question_uuid: UUID
    value: str


@dataclass
class PollAnswer:
    user: str
    key: str
    datetime: datetime
    poll_uuid: UUID
    answers: List[QuestionAnswer] = field(default_factory=list)

