from pathlib import Path
from datetime import datetime

def save_result(
    old: int,
    new: int,
    operation: str,
    coll_type: str
):
    file_path = Path(__file__).parent.parent.parent/"result"/"mongodb"/coll_type/f"{operation}.json"
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d, %H:%M:%S")

    result: dict = {
        "date": now_date,
        "operation": operation,
        "coll_type": coll_type,
    }
