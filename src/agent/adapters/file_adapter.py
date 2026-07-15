from pathlib import Path

from agent.core.file_discovery import FileDiscovery
from agent.models.prompt import Prompt

from .base import BaseAdapter


class FileAdapter(BaseAdapter):

    def extract(self, project_path: Path) -> list[Prompt]:

        prompts = []

        discovery = FileDiscovery(project_path)

        for file in discovery.discover():

            prompts.append(
                Prompt(
                    content=file.read_text(encoding="utf-8"),
                    source=file,
                )
            )

        return prompts
