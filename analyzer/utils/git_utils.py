from datetime import datetime
from git import Repo
from rich import print
import os

def repo_summary(repo):
    commits = list(repo.iter_commits())
    return {
        "repo_name": os.path.basename(repo.working_tree_dir),
        "total_commits": len(commits),
        "authors": {c.author.name for c in commits},
        "commit_messages": [c.summary.strip() for c in commits],
        "active_branches": [b.name for b in repo.branches],
    }

def get_commits_today(repo):
    today = datetime.now().date()
    return [c for c in repo.iter_commits() if c.committed_datetime.date() == today]

def average_commits_per_day(repo):
    commits = sorted(list(repo.iter_commits()), key=lambda c: c.committed_datetime)
    if not commits:
        return 0
    first_date = commits[0].committed_datetime.date()
    days = (datetime.now().date() - first_date).days + 1
    return len(commits) / days if days > 0 else len(commits)

def export_commits_today_md(repo, output_path=".", author=None):
    """Exports today's commits to a markdown file in the specified folder."""
    today = datetime.now().date()
    commits = [c for c in repo.iter_commits() if c.committed_datetime.date() == today]

    if author:
        commits = [c for c in commits if author.lower() in c.author.name.lower()]

    if not commits:
        print("[yellow]No commits found for today.[/yellow]")
        return

    date_str = today.strftime("%Y-%m-%d")
    filename = f"devlog-{date_str}.md"
    filepath = os.path.join(output_path, filename)

    lines = [f"# 🗓️ Dev Log — {date_str}\n"]

    for c in commits:
        time_str = c.committed_datetime.strftime("%H:%M")
        lines.append(f"## ✅ {c.summary.strip()}")
        lines.append(f"- ⏰ {time_str}")
        lines.append(f"- 👤 {c.author.name}")
        lines.append("")

    lines.append("## 🔚 End of Log")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def get_most_modified_files(repo, top_n=10):
    """Returns the top N most modified files in the repository."""
    file_changes = {}

    for commit in repo.iter_commits():
        for diff in commit.diff(commit.parents or None):
            if diff.a_path:
                file_changes[diff.a_path] = file_changes.get(diff.a_path, 0) + 1

    sorted_files = sorted(file_changes.items(), key=lambda x: x[1], reverse=True)
    return sorted_files[:top_n]
