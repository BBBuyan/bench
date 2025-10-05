from pathlib import Path
from datetime import datetime

suffix = "insert_unordered"

def save_result(durations: list[float], operation: str, coll_type: str):
    file_name = f"{coll_type}_{suffix}.txt"
    file_path = Path(__file__).parent.parent.parent/"result"/"mongodb"/file_name
    rounded = [round(d) for d in durations]

    with open(file_path, "a") as f:
        f.write(f"{operation:<20}: {str(rounded)}\n")

def mark_operation(coll_type: str):
    file_name = f"{coll_type}_{suffix}.txt"
    file_path = Path(__file__).parent.parent.parent/"result"/"mongodb"/file_name
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d, %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"{'':-<40}\n")
        f.write(now_date + "\n")

def mark_message(coll_type: str, msg: str):
    file_name = f"{coll_type}_{suffix}.txt"
    file_path = Path(__file__).parent.parent.parent/"result"/"mongodb"/file_name
    with open(file_path, "a") as f:
        f.write(msg + "\n")

