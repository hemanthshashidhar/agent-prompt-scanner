from pathlib import Path

from agent.core.project_loader import ProjectLoader
from agent.scanner.base import BaseScanner
from agent.scanner.result import ScanResult


class PromptScanner(BaseScanner):

    name = "Prompt Scanner"

    def scan(self, project_path: Path) -> ScanResult:
        loader = ProjectLoader(project_path)

        print(f"Loaded project: {loader.root()}")

        return ScanResult()
