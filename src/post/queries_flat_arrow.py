read_flat = """
select data
from flat
where (data -> 'error_count')::int = %s
"""

sort_flat = """
select data
from flat
where (data -> 'error_count')::int = %s
order by (data -> 'total_storage_gb')::int
"""

avg_flat = """
select avg((data -> 'total_storage_gb')::numeric)
from flat
where (data -> 'error_count')::int = %s
"""

update_flat ="""
update flat
set data = %s
where (data -> 'error_count')::int = %s
"""
