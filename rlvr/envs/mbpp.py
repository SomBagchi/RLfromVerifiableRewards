from pydantic import BaseModel


class MBPPTask(BaseModel):
    task_id: int
    prompt: str
    entry_point: str
    tests: list[str]


def load_mbpp_dev_split() -> list[MBPPTask]:
    """Return a small dev split (Session 2 populates this)."""
    return []


def render_prompt(task: MBPPTask, seed: int | None = None) -> str:
    """Return the prompt string for a generation request."""
    return task.prompt
