import argparse
from git import Repo
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from datetime import datetime, timedelta
import os
from analyzer.commands.dashboard import handle_dashboard
from analyzer.commands.summary import handle_summary

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

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
