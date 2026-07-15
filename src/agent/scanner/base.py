from abc import ABC, abstractmethod
from pathlib import Path

from agent.scanner.result import ScanResult


class BaseScanner(ABC):

    name: str = "Base Scanner"

    @abstractmethod
    def scan(self, project_path: Path) -> ScanResult:
        """Scan a project."""
        raise NotImplementedError
