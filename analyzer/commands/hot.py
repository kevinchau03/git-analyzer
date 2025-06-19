from git import Repo
from rich import print
from analyzer.utils.git_utils import get_most_modified_files

def handle_hot(args):
    repo = Repo(args.path)
    print(f":fire: [bold red]Fetching the hottest files in {repo.working_tree_dir}...[/bold red]")
    
    top_files = get_most_modified_files(repo, top_n=args.top_n)
    
    if not top_files:
        print("[yellow]No modified files found.[/yellow]")
        return
    
    print(":fire: [bold red]Most Modified Files:[/bold red]")
    for file, count in top_files:
        print(f"  - {file} (modified {count} times)")