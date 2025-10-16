from src.post.post_types import BasePost

def read_query(type: BasePost):
    query = f"select (data) from {type.name}"
    where = f" where (data #>> '{{ {type.model_path} }}')::int = %s"
    return query + where

def update_query(type: BasePost):
    return ""

def insert_query(type: BasePost):
    return ""

def avg_query(type: BasePost):
    return ""

def sort_query(type: BasePost):
    return ""
