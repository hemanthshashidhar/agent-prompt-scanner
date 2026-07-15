from pathlib import Path


class PromptDetector:

    PROMPT_FILE_NAMES = {
        "prompt",
        "prompts",
        "system_prompt",
        "system",
        "instructions",
        "instruction",
        "agent",
    }

    VALID_EXTENSIONS = {
        ".txt",
        ".md",
        ".prompt",
    }

    def is_prompt(self, file: Path) -> bool:

        if file.suffix.lower() not in self.VALID_EXTENSIONS:
            return False

        return file.stem.lower() in self.PROMPT_FILE_NAMES
