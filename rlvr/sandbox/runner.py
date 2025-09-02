from dataclasses import dataclass


@dataclass
class SandboxResult:
    passed: bool
    n_passed: int
    n_tests: int
    stdout: str = ""
    stderr: str = ""
    wall_time_s: float = 0.0


def run_in_sandbox(code: str, tests: list[str], cfg: dict | None = None) -> SandboxResult:
    """Stub sandbox; Session 3 replaces this with a real runner."""
    return SandboxResult(passed=False, n_passed=0, n_tests=len(tests))
