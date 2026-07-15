from pydantic import BaseModel, Field

from agent.models.finding import Finding


class ScanResult(BaseModel):
    findings: list[Finding] = Field(default_factory=list)

    def add(self, finding: Finding):
        self.findings.append(finding)
