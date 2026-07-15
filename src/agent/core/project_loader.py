from pathlib import Path


class ProjectLoader:
    def __init__(self, project_path: Path):
        self.project_path = project_path

    def exists(self) -> bool:
        return self.project_path.exists()

    def root(self) -> Path:
        return self.project_path.resolve()
