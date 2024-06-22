from dataclasses import dataclass
from uuid import UUID

@dataclass
class QuestionResult:
    question_uuid: UUID
    value: str