import argparse
from analyzer.commands.dashboard import handle_dashboard
from analyzer.commands.summary import handle_summary
from analyzer.commands.log import handle_log

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

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
