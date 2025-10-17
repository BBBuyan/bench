read_obj1 = """
select data
from obj1 
where (data -> 'l1'->>'error_count')::int = %s
"""

read_obj2 = """
select data
from obj2
where (data -> 'l1'->'l2'->>'error_count')::int = %s
"""

read_obj4 = """
select data
from obj4
where (data -> 'l1'->'l2'->'l3'->'l4'->>'error_count')::int = %s
"""

read_obj8 = """
select data
from obj8
where (data -> 'l1'->'l2'->'l3'->'l4'->'l5'->'l6'->'l7'->'l8'->>'error_count')::int = %s
"""

read = {
    1: read_obj1, 
    2: read_obj2,
    4: read_obj4,
    8: read_obj8,
}

sort_obj1 = """
select data
from obj1 
where (data -> 'l1'->>'error_count')::int = %s 
order by (data -> 'l1' ->> 'total_storage_gb')::int 
"""

sort_obj2 = """
select data
from obj2 
where (data -> 'l1'->'l2'->>'error_count')::int = %s 
order by (data -> 'l1'->'l2'->> 'total_storage_gb')::int 
"""

sort_obj4 = """
select data
from obj4 
where (data -> 'l1'->'l2'->'l3'->'l4'->>'error_count')::int = %s 
order by (data -> 'l1'->'l2'->'l3'->'l4'->> 'total_storage_gb')::int 
"""

sort_obj8 = """
select data
from obj8
where (data -> 'l1'->'l2'->'l3'->'l4'->'l5'->'l6'->'l7'->'l8'->>'error_count')::int = %s 
order by (data -> 'l1'->'l2'->'l3'->'l4'->'l5'->'l6'->'l7'->'l8'->> 'total_storage_gb')::int 
"""

sort = {
    1: sort_obj1, 
    2: sort_obj2,
    4: sort_obj4,
    8: sort_obj8,
}

avg_obj1 = """
select avg((data #>> '{l1,total_storage_gb}')::numeric)
from obj1
where (data -> 'l1'->>'error_count')::int = %s
"""

avg_obj2 = """
select avg((data #>> '{l1,l2,total_storage_gb}')::numeric)
from obj2
where (data -> 'l1'->'l2'->>'error_count')::int = %s
"""

avg_obj4 = """
select avg((data #>> '{l1,l2,l3,l4,total_storage_gb}')::numeric)
from obj4
where (data -> 'l1'->'l2'->'l3'->'l4'->>'error_count')::int = %s
"""

avg_obj8 = """
select avg((data #>> '{l1,l2,l3,l4,l5,l6,l7,l8,total_storage_gb}')::numeric)
from obj8
where (data -> 'l1'->'l2'->'l3'->'l4'->'l5'->'l6'->'l7'->'l8'->>'error_count')::int = %s
"""

avg = {
    1: avg_obj1, 
    2: avg_obj2,
    4: avg_obj4,
    8: avg_obj8,
}

update_storage_obj1 = """
update obj1
set data = %s
where (data -> 'l1'->>'error_count')::int = %s
"""

update_storage_obj2 = """
update obj2
set data = %s
where (data -> 'l1'->'l2'->>'error_count')::int = %s
"""

update_storage_obj4 = """
update obj4
set data = %s
where (data -> 'l1'->'l2'->'l3'->'l4'->>'error_count')::int = %s
"""

update_storage_obj8 = """
update obj8
set data = %s
where (data -> 'l1'->'l2'->'l3'->'l4'->'l5'->'l6'->'l7'->'l8'->>'error_count')::int = %s
"""

update_storage = {
    1: update_storage_obj1, 
    2: update_storage_obj2,
    4: update_storage_obj4,
    8: update_storage_obj8,
}
