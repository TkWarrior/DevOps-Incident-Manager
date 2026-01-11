from github import Github
import os

g = Github(os.getenv("GITHUB_TOKEN"))

# Function to create a pull request with the suggested code fix
def create_pr(repo_name, file_path, new_code):
    repo = g.get_repo(repo_name)
    file = repo.get_contents(file_path)

    repo.update_file(
        path=file_path,
        message="AI: Fix runtime error",
        content=new_code,
        sha=file.sha,
        branch="main"
    )

    pr = repo.create_pull(
        title="AI Fix: Runtime Error",
        body="Auto-generated fix by AI DevOps Agent",
        head="main",
        base="main"
    )

    return pr.html_url
