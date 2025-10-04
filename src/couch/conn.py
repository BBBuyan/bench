import os
from dotenv import load_dotenv
from src.base_types import Base, Arr, Flat, Obj

load_dotenv(dotenv_path=".env")

ip = os.getenv("COUCH_IP")
port = os.getenv("COUCH_PORT")
user = os.getenv("COUCH_USER")
password = os.getenv("COUCH_PASSWORD")
root_url = f"http://{user}:{password}@{ip}:{port}/"

levels = [1,2,4,8]
arr_list: list[Base] = [Arr(i) for i in levels]
obj_list: list[Base] = [Obj(i) for i in levels]
flat_list: list[Base] = [Flat()]
all_dbs: list[Base] = flat_list + obj_list + arr_list

if __name__ == "__main__":
    print(root_url)
