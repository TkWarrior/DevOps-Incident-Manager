import re # Regular expressions library

# Extract file name and line number from logs

def extract_line_number(logs):
    match = re.search(r"\.java:(\d+)", logs)
    if match:
        return int(match.group(1))
    return None

