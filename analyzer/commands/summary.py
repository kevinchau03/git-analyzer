from analyzer.utils.git_utils import repo_summary
from git import Repo
from rich import print
from rich.table import Table

def handle_summary(args):
    repo = Repo(args.path)
    summary = repo_summary(repo)

    print(f":mag: [bold green]Repository Summary for {summary['repo_name']}[/bold green]")
    print(f":sparkles: [green]Total commits:[/green] {summary['total_commits']}")
    print(f":busts_in_silhouette: [cyan]Authors:[/cyan] {', '.join(summary['authors'])}")
    print(f":memo: [yellow]Recent commit messages:[/yellow]")
    for msg in summary['commit_messages'][:5]:
        print(f"• {msg}")
