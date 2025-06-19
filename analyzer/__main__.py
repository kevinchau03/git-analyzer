import argparse
from analyzer.commands.dashboard import handle_dashboard
from analyzer.commands.summary import handle_summary
from analyzer.commands.log import handle_log
from analyzer.commands.hot import handle_hot

def main():
    parser = argparse.ArgumentParser(
        description="Git Commit Analyzer CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Summary command
    sp = subparsers.add_parser("summary", help="Repo summary")
    sp.add_argument("--path", default=".")
    sp.set_defaults(func=handle_summary)

    # Dashboard command
    dash = subparsers.add_parser("dashboard", help="Overview screen")
    dash.set_defaults(func=handle_dashboard)

    log_parser = subparsers.add_parser("log", help="Export today's commits to a markdown devlog")
    log_parser.add_argument("--path", default=".", help="Path to Git repository")
    log_parser.add_argument("--author", help="Filter by author name")
    log_parser.set_defaults(func=handle_log)

    # Hot command
    hot_parser = subparsers.add_parser("hot", help="Show the most-modified files in the repo")
    hot_parser.add_argument("--path", default=".", help="Path to Git repository")
    hot_parser.add_argument("--top-n", type=int, default=10, help="Number of top modified files to show")
    hot_parser.set_defaults(func=handle_hot)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
