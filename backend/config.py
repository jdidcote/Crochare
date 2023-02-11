from pathlib import Path
from dotenv import dotenv_values

PROJECT_ROOT_PATH: Path = Path(__file__).parent.parent

ENV_CONFIG: dict[str, any] = dict(
    dotenv_values(PROJECT_ROOT_PATH / ".env")
)