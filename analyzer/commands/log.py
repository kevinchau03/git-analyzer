from git import Repo
from analyzer.utils.git_utils import export_commits_today_md

def handle_log(args):
    repo = Repo(args.path)
    print(f":memo: [yellow]Printing todays work...[/yellow]")
    export_commits_today_md(repo, output_path=args.path, author=args.author)
