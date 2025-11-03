import os
from pathlib import Path
from dotenv import load_dotenv
import pytest

# Resolve the path to tests/.env.test
_TESTS_DIR = Path(__file__).parent
_ENV_PATH = _TESTS_DIR / ".env.test"

# Load variables into process env before any tests run
load_dotenv(dotenv_path=_ENV_PATH, override=True)

# (optional) sanity check, can be removed later
if not os.getenv("API_KEY"):
    raise RuntimeError(f"Failed to load {_ENV_PATH}")

def pytest_addoption(parser):
    parser.addoption(
        "--llmtests", action="store_true", default=False, help="run slow tests"
    )

# def pytest_configure(config):
#     config.addinivalue_line("markers", "llmtest: mark test as slow")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--llmtests"):
        # --runslow given: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --llmtests option to run")
    for item in items:
        if "llmtest" in item.keywords:
            item.add_marker(skip_slow)