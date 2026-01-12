from github import Github
import os
from utils.extract_line_number import extract_line_number
from utils.find_method import find_method

def get_broken_method(repo_name, file_path, logs):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(repo_name)

    file = repo.get_contents(file_path)
    source = file.decoded_content.decode()

    line_no = extract_line_number(logs)
    if not line_no:
        raise Exception("Could not extract line number from logs")

    start, end = find_method(source, line_no)
    broken_method = "\n".join(source.split("\n")[start:end+1])

    return broken_method, source, start, end
