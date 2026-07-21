from rich import print

from agent.scanner.result import ScanResult


class ReportRenderer:

    def render(self, result: ScanResult) -> None:

        print()
        print("[bold cyan]Agent Verify[/bold cyan]")
        print("=" * 40)

        if not result.findings:
            print("[green]✓ No findings found.[/green]")
            return

        print(f"[bold red]Findings ({len(result.findings)})[/bold red]")
        print()

        for finding in result.findings:
            print(f"[bold]{finding.id}[/bold] [{finding.severity.value}]")
            print(f"Title          : {finding.title}")
            print(f"File           : {finding.file}")
            print(f"Description    : {finding.description}")
            print(f"Recommendation : {finding.recommendation}")
            print()
