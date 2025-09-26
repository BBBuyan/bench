import datetime
from pathlib import Path
import json

def mark_empty_space(file_name):
    file_path = Path(__file__).parent.parent.parent/"result"/f"{file_name}.json"
    with open(file_path, "a") as f:
        f.write("\n")

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
