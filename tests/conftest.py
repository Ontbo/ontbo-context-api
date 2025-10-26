import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve the path to tests/.env.test
_TESTS_DIR = Path(__file__).parent
_ENV_PATH = _TESTS_DIR / ".env.test"

# Load variables into process env before any tests run
load_dotenv(dotenv_path=_ENV_PATH, override=True)

# (optional) sanity check, can be removed later
if not os.getenv("API_KEY"):
    raise RuntimeError(f"Failed to load {_ENV_PATH}")

