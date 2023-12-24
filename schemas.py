from typing import List, Dict

from pydantic import BaseModel, model_validator, field_validator


class BaseSurvey(BaseModel):
    questionsAndAnswers: Dict[str, str]
    _required_questions: List[str] = []

    _required_questions: List[str] = ["your full name", "your email", "are you a CU graduate?", "which program did you study?", "would you be willing to enroll in a master's degree program in 2024?"]
