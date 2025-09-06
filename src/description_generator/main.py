import requests
from conn import url, headers, my_data

def get_descriptions():
    r = requests.post(url, headers=headers, json=my_data)
    data: dict = r.json()
    doc = data["content"]["text"]
    print(" | ", end="", flush=True)
    return doc

def save(lines):
    with open("descriptions.json", "a") as f:
        for line in lines:
            f.write(line + "\n")
    print(len(lines), end=", ", flush=True)

def execute_100():
    descs: str = get_descriptions()
    lines = descs.splitlines()
    save(lines)

def main():
    print("---STARTED---")
    for i in range(50):
        print(i, end="", flush=True)
        execute_100()
    print("\n---DONE---")

main()
