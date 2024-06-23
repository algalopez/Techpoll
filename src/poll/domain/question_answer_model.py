from dataclasses import dataclass
from uuid import UUID

@dataclass
class QuestionAnswer:
    question_uuid: UUID
    value: str