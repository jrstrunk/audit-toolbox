import subprocess
import datetime

def get_git_file_info(f: str):
    # Get the commit history for the file
    commits = subprocess.check_output(['git', 'log', '--pretty=format:%ai', f]).decode('utf-8').split('\n')

    # Calculate the number of days between the first and most recent commit
    dates = [datetime.datetime.strptime(commit.split()[0], '%Y-%m-%d') for commit in commits]
    days_between = (max(dates) - min(dates)).days

    # Get the number of lines that have been cumulatively deleted for all the commits in the file
    deletions = subprocess.check_output(['git', 'log', '--pretty=tformat:', '--numstat', f]).decode('utf-8').split('\n')
    total_deletions = sum(int(deletion.split()[1]) for deletion in deletions if deletion)
    total_additions = sum(int(deletion.split()[0]) for deletion in deletions if deletion)

    # Get the number of authors that worked on the file
    authors = subprocess.check_output(['git', 'shortlog', '-sne', '--', f]).decode('utf-8').split('\n')
    num_authors = len(authors) - 1  # Subtract 1 to ignore the final empty string

    return {
        "name": f,
        "ratio": total_deletions / total_additions if total_additions > 0 else 0.0,
        "adds": total_additions,
        "dels": total_deletions,
        "days": days_between,
        "authors": num_authors,
    }
