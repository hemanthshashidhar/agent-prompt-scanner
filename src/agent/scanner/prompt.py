from pathlib import Path

from agent.adapters.file_adapter import FileAdapter
from agent.scanner.base import BaseScanner
from agent.scanner.result import ScanResult


class PromptScanner(BaseScanner):

    name = "Prompt Scanner"

    def scan(self, project_path: Path) -> ScanResult:

        adapter = FileAdapter()

        prompts = adapter.extract(project_path)

        print()

        print("Detected Prompts")

        print("----------------")

        for prompt in prompts:
            print(prompt.source.relative_to(project_path))

        return ScanResult()
