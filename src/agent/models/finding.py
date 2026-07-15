from pathlib import Path

from pydantic import BaseModel

from agent.models.severity import Severity


class Finding(BaseModel):
    id: str
    title: str

    severity: Severity

    description: str

    recommendation: str

    file: Path | None = None

    line: int | None = None
