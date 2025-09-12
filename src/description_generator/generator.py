from .exec_type import ExecType
from .conn import url, headers, description_payload, info_payload
import requests
from pathlib import Path
import threading
from time import time

def call_ai(payload) -> requests.Response:
    return requests.post(url, headers=headers, json=payload)

def get_ai_data(payload) -> list[str]:
    r = call_ai(payload)
    data: dict = r.json()
    doc: str = data["content"]["text"]
    return doc.splitlines()

def save_ai_data(lines: list[str], type: ExecType, thread_id: int | None = None):
    print("  ---SAVING " , end="", flush=True)
    file_name = type.value
    if thread_id is not None:
        file_name += f"_{thread_id}"

    file_path =  Path(__file__).parent.parent.parent/"data"/f"{file_name}.json"
    with open(file_path, "a") as f:
        for line in lines:
            f.write(line + "\n")
    print("SAVED---")

def sequential_exec(type: ExecType = ExecType.INFO):
    print("---SEQUENTIAL EXECUTION STARTED---")
    payload = info_payload
    if type == ExecType.DESCRIPTION:
        payload = description_payload

    start = time()
    ai_data = get_ai_data(payload)
    end = time()
    print("---ENDED---")
    print(f"Took: {end-start:.0f} s")
    save_ai_data(ai_data, type)

def thread_generate_ai_data(thread_id: int, type: ExecType):
    payload = info_payload
    if type == ExecType.DESCRIPTION:
        payload = description_payload

    ai_data = get_ai_data(payload)
    save_ai_data(ai_data, type, thread_id)

def concurrent_exec(type: ExecType = ExecType.INFO):
    print("---CONCURRENT EXECUTION STARTED---")
    t_list: list[threading.Thread] = []
    num_of_threads = 4
    for i in range(num_of_threads):
        t = threading.Thread(target=thread_generate_ai_data, args=(i, type))
        t_list.append(t)

    start = time()
    for t in t_list:
        t.start()

    for t in t_list:
        t.join()
    end = time()

    print("---ENDED---")
    print(f"Took: {end-start:.0f} s")
    thread_result_combine(num_of_threads, type)

def thread_result_combine(num_of_threads: int, type: ExecType):
    output_file_path =  Path(__file__).parent.parent.parent/"data"/f"{type.value}.json"
    with open(output_file_path, "a") as out_file:
        for i in range(num_of_threads):
            thread_description_path = Path(__file__).parent.parent.parent/"data"/f"{type.value}_{i}.json"

            with open(thread_description_path, "r") as in_file:
                out_file.write(in_file.read())

            thread_description_path.unlink()
