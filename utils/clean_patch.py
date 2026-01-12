import re

def clean_patch(patch):
    return re.sub(r"```[\w]*", "", patch).strip()
