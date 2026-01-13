# from log_reader.log_reader import fetch_logs
# from graph.graph import agent
# from agent.github_agent import create_pr
# from utils.get_broken_method import get_broken_method
# from utils.clean_patch import clean_patch
# setverbose = True
# setdebug = True

# if __name__ == "__main__":
    
#     logs = fetch_logs()
    
#     repo_name = "TkWarrior/crash_simulator"
#     file_path = "src/main/java/com/example/demo/controller/CrashController.java"
    
#     broken_method,source,start,end = get_broken_method(repo_name, file_path ,logs)
    
#     print("Invoking AI DevOps Agent...\n")
#     print("📝 LOGS:\n", logs)
#     print("\n🔧 BROKEN METHOD:\n", broken_method)
    
#     result = agent.invoke({
#         "logs": logs,
#         "broken_method": broken_method
#     })

#     print("\n🧠 ERROR:", result["error_summary"])
#     print("\n🔍 ROOT CAUSE:", result["root_cause"])
#     print("\n🛠 FIX:", result["fix"])
#     print("\n� RAW PATCH:\n", result["patch"])
    
#     patch_code = clean_patch(result["patch"])
#     print("\n� CLEAN PATCH:\n", patch_code)
    
#     pull_request_url = create_pr(repo_name , file_path , logs ,patch_code)
    
#     print("pull request created at:", pull_request_url)

from log_reader.log_reader import fetch_logs,extract_recent_error
from graph.graph import agent
from agent.github_agent import create_pr
from utils.get_broken_method import get_broken_method
from utils.clean_patch import clean_patch
from utils.extract_line_number import extract_line_number

def run_agent():
    
    logs = fetch_logs()
    recent_logs = extract_recent_error(logs)
    repo_name = "TkWarrior/crash_simulator"
    file_path = "src/main/java/com/example/demo/controller/CrashController.java"
    broken_method, source, start, end = get_broken_method(repo_name, file_path, recent_logs)
    print("LOG SAYS ERROR HERE:", extract_line_number(logs))
    print("METHOD WE ARE PATCHING:\n", broken_method)
    
    result = agent.invoke({
        "logs": recent_logs,
        "broken_method": broken_method
    })

    patch_code = clean_patch(result["patch"])

    pr_url = create_pr(repo_name, file_path, logs, patch_code)

    return {
        "logs": logs,
        "error": result["error_summary"],
        "root_cause": result["root_cause"],
        "patch": patch_code,
        "pr": pr_url
    }
