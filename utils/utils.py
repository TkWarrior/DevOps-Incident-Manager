import re # Regular expressions library

# Extract file name and line number from logs

def extract_line_number(logs):
    match = re.search(r"\.java:(\d+)", logs)
    if match:
        return int(match.group(1))
    return None

# def extract_location(logs):
#     match = re.search(r"\(([^:]+\.java):(\d+)\)", logs)
#     if match:
#         return match.group(1), int(match.group(2))
#     return None, None

# Find the method in the source code given a line number
def find_method(source, line_no):
    lines = source.split("\n")
    
    if line_no is None:
        raise Exception("Unable to extract line number from logs.\n")
    
    start = line_no - 1

    while start >= 0 and "public" not in lines[start]:
        start -= 1

    brace = 0
    end = start
    for i in range(start, len(lines)):
        if "{" in lines[i]:
            brace += 1
        if "}" in lines[i]:
            brace -= 1
        if brace == 0 and i > start:
            end = i
            break

    return start, end

# Replace the method in the source code with the new method
def replace_method(source, start, end, new_method):
    
    lines = source.split("\n")
    return "\n".join(
        lines[:start] +
        [new_method] +
        lines[end+1:]
    )
