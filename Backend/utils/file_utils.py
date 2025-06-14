import subprocess
import os

def clone_repo(repo_url, dest="cloned_repos"):
    os.makedirs(dest, exist_ok=True)
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    clone_path = os.path.join(dest, repo_name)
    subprocess.run(["git", "clone", repo_url, clone_path])
    return clone_path
