from dataclasses import dataclass


@dataclass
class Generation:
    task_id: int
    code: str


def generate_candidates(prompt: str, n: int = 1) -> list[Generation]:
    """Return zero or more candidates; Session 5 wires real models."""
    return []
