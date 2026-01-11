import requests
from llm import ask

def fetch_logs():
    url = "http://localhost:8080/crash/logs"
    r = requests.get(url)
    return r.text

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