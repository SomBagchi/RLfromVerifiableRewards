import importlib
import pathlib
import subprocess
import sys


def test_python_version():
    assert sys.version_info[:2] >= (3, 11)


def test_import_stubs():
    # import every submodule to ensure wiring is sound
    pkgs = [
        "rlvr",
        "rlvr.envs.mbpp",
        "rlvr.sandbox.runner",
        "rlvr.rewards.code_tests",
        "rlvr.sampling.generate",
        "rlvr.training.awr",
        "rlvr.training.ppo_lite",
        "rlvr.eval.report",
        "rlvr.utils.jax_helpers",
    ]
    for m in pkgs:
        importlib.import_module(m)


def test_cli_entrypoints_exist():
    root = pathlib.Path(__file__).resolve().parents[1]
    for f in ["run_demo.py", "run_eval.py", "run_awr.py", "run_ppo.py"]:
        proc = subprocess.run(
            [sys.executable, str(root / "scripts" / f), "--help"], capture_output=True, check=False
        )
        assert proc.returncode == 0, f"{f} --help failed: {proc.stderr.decode()}"
