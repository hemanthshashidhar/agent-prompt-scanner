from pydantic import BaseModel, Field

from agent.models.finding import Finding


class Report(BaseModel):
    findings: list[Finding] = Field(default_factory=list)

    @property
    def total_findings(self) -> int:
        return len(self.findings)
