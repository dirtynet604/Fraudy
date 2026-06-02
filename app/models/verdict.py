from pydantic import BaseModel

class Verdict(BaseModel):
    risk_score: float
    category: str
    confidence: float
    explanation: str