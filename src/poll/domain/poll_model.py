from dataclasses import dataclass
from uuid import UUID
from typing import List

@dataclass
class PollQuestionOption:
    id: int
    question_uuid: UUID
    name: str
    value: str

@dataclass
class PollQuestion:
    uuid: UUID
    poll_uuid: UUID
    topic: str
    description: str
    enabled: bool
    options: List[PollQuestionOption]

@dataclass
class Poll:
    uuid: UUID
    name: str
    description: str
    questions: List[PollQuestion]
