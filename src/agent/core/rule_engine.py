from agent.models.prompt import Prompt
from agent.rules.base import BaseRule


class RuleEngine:

    def __init__(self, rules: list[BaseRule]):
        self.rules = rules

    def run(self, prompt: Prompt):

        findings = []

        for rule in self.rules:

            finding = rule.check(prompt)

            if finding:
                findings.append(finding)

        return findings
