from github import Github
import os
from utils.utils import extract_line_number, find_method, replace_method

g = Github(os.getenv("GITHUB_TOKEN"))

# agent pull request karega with the suggested code fix
# Function to create a pull request with the suggested code fix
def create_pr(repo_name, file_path, logs ,patch_code):
    # get the repository name
    repo = g.get_repo(repo_name)
    # get the main branch
    base = repo.get_branch("main")
    # craete a new branch from main
    branch_name = "ai-fix-branch"
    
    # Create branch if it doesn't exist
    try:
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base.commit.sha)
    except:
        pass  # branch already exists
    
    # Get the broken method details--file content, method start and end lines
    broken_method, original, start ,end = broken_method(repo_name, file_path ,logs)
   
    # Replace the method with the patch code
    updated = replace_method(original, start, end, patch_code)
    
    file = repo.get_contents(file_path, ref=branch_name)
    # commit to AI branch in the repository
    repo.update_file(
        path=file_path,
        message="AI: Fix runtime error",
        content=updated,
        sha=file.sha,
        branch=branch_name
    )
    
    # Create a pull request
    pr = repo.create_pull(
        title="AI Fix: Runtime Error",
        body="Auto-generated fix by AI DevOps Agent",
        head=branch_name,
        base="main"
    )
    # Return the pull request URL
    return pr.html_url
