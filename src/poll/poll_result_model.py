from src.poll.question_result_model import QuestionResult
from dataclasses import dataclass, field
from uuid import UUID
from typing import List

@dataclass
class PollResult:
    poll_uuid: UUID
    answers: List[QuestionResult] = field(default_factory=list)
