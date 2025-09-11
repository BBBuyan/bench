from .conn import url, headers, my_data
import requests
from pathlib import Path
import threading

def save(lines: list[str]):
    print("  ---SAVING " , end="", flush=True)
    description_path =  Path(__file__).parent.parent.parent/"data"/"descriptions.json"
    with open(description_path, "a") as f:
        for line in lines:
            f.write(line + "\n")
    print("SAVED---")

def call_ai() -> requests.Response:
    return requests.post(url, headers=headers, json=my_data)

def get_descriptions()->list[str]:
    r = call_ai()
    data: dict = r.json()
    doc: str = data["content"]["text"]
    return doc.splitlines()

# batch is 40
def execute_batch():
    descs: list[str] = get_descriptions()
    save(descs)

def thread_save(lines: list[str], thread_id: int):
    description_path =  Path(__file__).parent.parent.parent/"data"/f"descriptions_{thread_id}.json"
    with open(description_path, "a") as f:
        for line in lines:
            f.write(line + "\n")

def thread_execute_batch(thread_id: int):
    descs: list[str] = get_descriptions()
    thread_save(descs, thread_id)

def thread_main():
    t_list: list[threading.Thread] = []
    for i in range(4):
        t = threading.Thread(target=thread_execute_batch, args=(i,))
        t_list.append(t)

    for t in t_list:
        t.start()

    for t in t_list:
        t.join()

