import requests
from llm import ask

def fetch_logs():
    url = "http://localhost:8080/crash/logs"
    r = requests.get(url)
    return r.text

def extract_recent_error(logs, max_lines=50):
    lines = logs.split("\n")

    # find last ERROR or Exception
    for i in range(len(lines)-1, -1, -1):
        if "Exception" in lines[i] or "ERROR" in lines[i]:
            start = max(0, i - max_lines)
            return "\n".join(lines[start:i+1])

    # fallback: last 100 lines
    return "\n".join(lines[-100:])

def has_error(logs):
    return "Exception" in logs or "ERROR" in logs

if __name__ == "__main__":
    logs = fetch_logs()
   
    if has_error(logs):
        print("crash detected:")
        # print(logs)
    else:
        print("No errors found in logs.")
    
    # print(ask("what is the summary of the following logs?\n" + logs))
    
    print(ask(logs))