from pathlib import Path

from agent.core.file_discovery import FileDiscovery
from agent.scanner.base import BaseScanner
from agent.scanner.result import ScanResult


class PromptScanner(BaseScanner):

    name = "Prompt Scanner"

    def scan(self, project_path: Path) -> ScanResult:

        discovery = FileDiscovery(project_path)

        files = discovery.discover()

        print()

        print("Prompt Files")

        print("------------")

        for file in files:
            print(file.relative_to(project_path))

        return ScanResult()
