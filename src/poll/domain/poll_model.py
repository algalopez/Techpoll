from dataclasses import dataclass
from uuid import UUID
from typing import List

@dataclass
class PollQuestionOptions:
    id: int
    question_uuid: UUID
    options: dict

@dataclass
class PollQuestions:
    uuid: UUID
    poll_uuid: UUID
    topic: str
    description: str
    enabled: bool
    options: List[PollQuestionOptions]

@dataclass
class Poll:
    uuid: UUID
    name: str
    description: str
    questions: List[PollQuestions]
