from pathlib import Path

from agent.core.prompt_detector import PromptDetector


class FileDiscovery:

    PATTERNS = [
        "*.md",
        "*.txt",
        "*.prompt",
    ]

    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.detector = PromptDetector()

    def discover(self) -> list[Path]:

        files = []

        for pattern in self.PATTERNS:
            files.extend(self.project_path.rglob(pattern))

        return sorted(
            {
                file
                for file in files
                if self.detector.is_prompt(file)
            }
        )
