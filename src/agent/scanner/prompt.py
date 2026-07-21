from pathlib import Path

from agent.adapters.file_adapter import FileAdapter
from agent.core.rule_engine import RuleEngine
from agent.rules.prompt.registry import get_prompt_rules
from agent.scanner.base import BaseScanner
from agent.scanner.result import ScanResult


class PromptScanner(BaseScanner):

    name = "Prompt Scanner"

    def scan(self, project_path: Path) -> ScanResult:

        adapter = FileAdapter()
        prompts = adapter.extract(project_path)

        engine = RuleEngine(
            rules=get_prompt_rules()
        )

        result = ScanResult()

        for prompt in prompts:

            findings = engine.run(prompt)

            result.findings.extend(findings)

        return result
