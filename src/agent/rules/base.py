from abc import ABC, abstractmethod

from agent.models.finding import Finding
from agent.models.prompt import Prompt
from agent.models.rule import Rule


class BaseRule(ABC):

    rule: Rule

    @abstractmethod
    def check(self, prompt: Prompt) -> list[Finding]:
        pass
