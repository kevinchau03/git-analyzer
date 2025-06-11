from git import Repo
from rich import print
from analyzer.utils.git_utils import export_commits_today_md

def handle_log(args):
    repo = Repo(args.path)
    print(f":memo: [green]Printing todays work...[/green]")
    export_commits_today_md(repo, output_path=args.path, author=args.author)
