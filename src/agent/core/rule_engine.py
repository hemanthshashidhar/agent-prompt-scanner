from agent.models.finding import Finding
from agent.models.prompt import Prompt
from agent.rules.base import BaseRule


class RuleEngine:

    def __init__(self, rules: list[BaseRule]):
        self.rules = rules

    def run(self, prompt: Prompt) -> list[Finding]:

        findings: list[Finding] = []

        for rule in self.rules:
            findings.extend(rule.check(prompt))

        return findings
