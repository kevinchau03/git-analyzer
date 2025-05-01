import argparse
from git import Repo
from rich import print

def main():
    parser = argparse.ArgumentParser(description="Git Commit Analyzer")
    parser.add_argument('--path', type=str, default='.', help='Path to Git repo')
    args = parser.parse_args()

    try:
        repo = Repo(args.path)
        commits = list(repo.iter_commits())
        print(f":sparkles: [green]Total commits:[/green] {len(commits)}")
    except Exception as e:
        print(f"[red]Error:[/red] {e}")

if __name__ == '__main__':
    main()
