# import re # Regular expressions library

# # Extract file name and line number from logs

# def extract_line_number(logs):
#     match = re.search(r"CrashController\.java:(\d+)", logs)
#     if match:
#         return int(match.group(1))
#     return None

import re

def extract_line_number(logs):
    for line in logs.splitlines():
        if "com.example.demo.controller.CrashController" in line:
            match = re.search(r"CrashController\.java:(\d+)", line)
            if match:
                return int(match.group(1))
    return None
