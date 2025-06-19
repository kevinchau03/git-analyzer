# Git Analyzer CLI

## What It Is:

A modern, modular command-line tool that helps developers gain insight into their Git commit history and personal coding patterns.

It enables users to track their own productivity, generate daily commit logs, and view clean summaries of their work — all from the terminal.


## 📦 Installation

```bash
pip install https://github.com/kevinchau03/git-analyzer.git
```

## 🚀 Key Features

| Command                    | Description                                       |
| -------------------------- | ------------------------------------------------- |
| `dashboard`                | Overview of the CLI tool and available commands   |
| `summary`                  | Shows total commits, authors, and recent messages |
| `author`                   | Filters commits by author                         |
| `today`                    | Lists all commits made today                      |
| `average`                  | Calculates average commits per day                |
| `log`                      | Exports today’s commits to a Markdown file        |
| *(Coming soon)* `hotspots` | Highlights most frequently modified files         |

## Technical Stack

Built with Python, using argparse, GitPython, and rich for a beautiful CLI experience