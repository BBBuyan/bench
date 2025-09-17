import datetime
from pathlib import Path
import json

def mark_end(file_name: str):
    with open(f"result/{file_name}.txt", "a") as f:
        f.write(f"{'':-<45}")
        f.write("\n")

def mark_operation(operation: str, file_name: str):
    now = datetime.datetime.now()
    file_path = Path(__file__).parent.parent.parent/"result"/f"{file_name}.txt"

    with open(file_path, "a") as f:
        f.write("\n")
        f.write(now.strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        f.write(f"{operation:-^45}\n")

def calc_diffs(old: list[float], new: list[float], operation: str):
    depth_list = [1, 2, 4, 8]
    print(f"##{operation}")
    print(f"{'':-<45}")
    print(f"|{'depth':^10}|{'before':^10}|{'after':^10}|{'diff':^10}|")
    print(f"|{'':-^10}|{'':-^10}|{'':-^10}|{'':-^10}|")
    for i in range(len(old)):
        old_val = old[i]
        new_val = new[i]
        diff = ((new_val - old_val)/old_val)*100
        print(f"|{depth_list[i]:^10}|{old[i]:>10.0f}|{new[i]:>10.0f}|{diff:>10.0f}|")
    print(f"{'':-<45}")

def save_result(
        old: list[float], 
        new: list[float], 
        operation: str, 
        file_name: str,
        coll_type: str
):
    file_path = Path(__file__).parent.parent.parent/"result"/f"{file_name}.json"
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%m-%d, %H:%M:%S")

    result: dict = {
        "date": now_date,
        "operation": operation,
        "coll_type": coll_type,
    }

    for i in range(len(old)):
        result[f"depth_{i}"] = {
            "before": round(old[i]),
            "after": round(new[i])
        }

    with open(file_path, "a") as f:
        json.dump(result, f)
        f.write("\n")

def save_es_result(
        old: list[float], 
        operation: str, 
        file_name: str,
        coll_type: str
):
    file_path = Path(__file__).parent.parent.parent/"result"/f"{file_name}.json"
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%m-%d, %H:%M:%S")

    result: dict = {
        "date": now_date,
        "coll_type": coll_type,
        "operation": operation,
    }

    for i in range(len(old)):
        result[f"depth_{i}"] = round(old[i])

    with open(file_path, "a") as f:
        json.dump(result, f)
        f.write("\n")
