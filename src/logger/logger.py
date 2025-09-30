import datetime
from pathlib import Path
import json

def save_result(
    old: list[float], 
    operation: str, 
    db_type: str,
    coll_type: str
):
    file_path = Path(__file__).parent.parent.parent/"result"/db_type/coll_type/f"{operation}.json"
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%m-%d, %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(now_date + "\n")

        for i in range(len(old)):
            f.write(f"d_{i}")


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
