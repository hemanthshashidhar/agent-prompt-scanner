from agent.models.finding import Finding
from agent.models.prompt import Prompt
from agent.models.severity import Severity
from agent.rules.base import BaseRule


class PR002(BaseRule):

    id = "PR002"
    title = "Prompt Role Override"

    PATTERNS = [
        "forget your instructions",
        "forget everything above",
        "act as",
        "pretend to be",
        "new instructions",
    ]

    def check(self, prompt: Prompt) -> Finding | None:

        content = prompt.content.lower()

        for pattern in self.PATTERNS:
            if pattern in content:
                return Finding(
                    id=self.id,
                    title=self.title,
                    severity=Severity.MEDIUM,
                    description=f'Found "{pattern}"',
                    recommendation="Review the prompt for role or instruction override attempts.",
                    file=prompt.source,
                )

        return None
