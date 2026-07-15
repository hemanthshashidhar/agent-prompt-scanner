from abc import ABC, abstractmethod
from pathlib import Path

from agent.models.prompt import Prompt


class BaseAdapter(ABC):

    @abstractmethod
    def extract(self, project_path: Path) -> list[Prompt]:
        pass
