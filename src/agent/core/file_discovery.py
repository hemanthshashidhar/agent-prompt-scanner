from pathlib import Path


class FileDiscovery:
    PROMPT_PATTERNS = [
        "*.md",
        "*.txt",
        "*.prompt",
    ]

    def __init__(self, project_path: Path):
        self.project_path = project_path

    def discover(self) -> list[Path]:
        files: list[Path] = []

        for pattern in self.PROMPT_PATTERNS:
            files.extend(self.project_path.rglob(pattern))

        return sorted(set(files))
