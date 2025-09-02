from pydantic import BaseModel


class EvalReport(BaseModel):
    total: int
    passed: int
    failed: int


def to_json(obj: EvalReport) -> str:
    return "{}"
