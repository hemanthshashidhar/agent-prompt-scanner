from agent.models.finding import Finding
from agent.models.prompt import Prompt
from agent.models.severity import Severity
from agent.rules.base import BaseRule


class PR001(BaseRule):
    id = "PR001"
    title = "Instruction Override"

    PATTERNS = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "disregard previous instructions",
    ]

    def check(self, prompt: Prompt) -> list[Finding]:
        findings: list[Finding] = []

        content = prompt.content.lower()

        for pattern in self.PATTERNS:
            if pattern in content:
                findings.append(
                    Finding(
                        id=self.id,
                        title=self.title,
                        severity=Severity.HIGH,
                        description=f'Found "{pattern}"',
                        recommendation="Remove instruction override.",
                        file=prompt.source,
                    )
                )

        return findings
