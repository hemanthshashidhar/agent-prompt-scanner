from abc import ABC, abstractmethod

from agent.models.finding import Finding
from agent.models.prompt import Prompt


class BaseRule(ABC):

    id: str
    title: str

    @abstractmethod
    def check(self, prompt: Prompt) -> Finding | None:
        pass
