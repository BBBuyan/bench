import os
from datetime import datetime
from pathlib import Path

ip = os.getenv("COUCH_IP")
suffix = ""
dir_name="thrash"

if ip == "10.214.0.4":
    dir_name = "result_cluster_q8_n1"
if ip == "10.214.0.8":
    dir_name = "result_alone"

def save_result(durations: list[float], operation: str, coll_type: str):
    file_path = Path(__file__).parent/dir_name/f"{coll_type}_{suffix}.txt"
    rounded = [round(d) for d in durations]

    with open(file_path, "a") as f:
        f.write(f"{operation:<30}: {str(rounded)}\n")

def mark_operation(coll_type: str):
    file_path = Path(__file__).parent/dir_name/f"{coll_type}_{suffix}.txt"
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d, %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"{'':-<40}\n")
        f.write(f"{now_date} + {ip}\n")

def mark_message(coll_type: str, msg: str):
    file_path = Path(__file__).parent/dir_name/f"{coll_type}_{suffix}.txt"
    with open(file_path, "a") as f:
        f.write(msg + "\n")

