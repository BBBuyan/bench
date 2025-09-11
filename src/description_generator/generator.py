from .conn import url, headers, my_data
import requests
from pathlib import Path

def get_descriptions()->list[str]:
    r = requests.post(url, headers=headers, json=my_data)
    data: dict = r.json()
    doc: str = data["content"]["text"]
    return doc.splitlines()

def save(lines: list[str]):
    print("  ---SAVING " , end="", flush=True)
    description_path =  Path(__file__).parent.parent.parent/"data"/"descriptions.json"
    with open(description_path, "a") as f:
        for line in lines:
            f.write(line + "\n")
    print("SAVED---")

def execute_100():
    descs: list[str] = get_descriptions()
    save(descs)
