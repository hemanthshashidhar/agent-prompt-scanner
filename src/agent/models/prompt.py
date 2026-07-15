from pathlib import Path

from pydantic import BaseModel


class Prompt(BaseModel):
    content: str
    source: Path
