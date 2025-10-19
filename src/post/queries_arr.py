read_arr1 = """
select data
from arr1 
where data @@ '$.a1[*].error_count == %s'
"""

read_arr2 = """
select data
from arr2
where data @@ '$.a1[*].a2[*].error_count == %s'
"""

read_arr4 = """
select data
from arr4
where data @@ '$.a1[*].a2[*].a3[*].a4[*].error_count == %s'
"""
read_arr8 = """
select data
from arr8
where data @@ '$.a1[*].a2[*].a3[*].a4[*].a5[*].a6[*].a7[*].a8[*].error_count == %s'
"""

read = {
    1: read_arr1, 
    2: read_arr2,
    4: read_arr4,
    8: read_arr8,
}

sort_arr1 = """
select a1_el
from arr1, 
jsonb_array_elements(data -> 'a1') as a1_el 
where (a1_el @> '{"error_count": %s}')
order by (a1_el ->>'total_storage_gb')::int"""

sort_arr2 = """select a2_el
from arr2, 
jsonb_array_elements(data -> 'a1') as a1_el,
jsonb_array_elements(a1_el -> 'a2') as a2_el 
where (a2_el @> '{"error_count": %s}')
order by (a2_el ->>'total_storage_gb')::int"""

sort_arr4 = """select a4_el
from arr4, 
jsonb_array_elements(data -> 'a1') as a1_el,
jsonb_array_elements(a1_el -> 'a2') as a2_el,
jsonb_array_elements(a2_el -> 'a3') as a3_el,
jsonb_array_elements(a3_el -> 'a4') as a4_el 
where (a4_el @> '{"error_count": %s}')
order by (a4_el ->>'total_storage_gb')::int"""

sort_arr8 = """select a8_el
from arr8, 
jsonb_array_elements(data -> 'a1') as a1_el,
jsonb_array_elements(a1_el -> 'a2') as a2_el,
jsonb_array_elements(a2_el -> 'a3') as a3_el,
jsonb_array_elements(a3_el -> 'a4') as a4_el,
jsonb_array_elements(a4_el -> 'a5') as a5_el,
jsonb_array_elements(a5_el -> 'a6') as a6_el,
jsonb_array_elements(a6_el -> 'a7') as a7_el,
jsonb_array_elements(a7_el -> 'a8') as a8_el 
where (a8_el @> '{"error_count": %s}')
order by (a8_el ->>'total_storage_gb')::int"""

sort = {
    1: sort_arr1, 
    2: sort_arr2,
    4: sort_arr4,
    8: sort_arr8,
}

avg_arr1 = """select avg((a1_el->>'total_storage_gb')::numeric)
from arr1, 
jsonb_array_elements(data -> 'a1') as a1_el 
where (a1_el @> '{"error_count": %s}')"""

avg_arr2 = """select avg((a2_el->>'total_storage_gb')::numeric)
from arr2, 
jsonb_array_elements(data -> 'a1') as a1_el,
jsonb_array_elements(a1_el -> 'a2') as a2_el
where (a2_el @> '{"error_count": %s}')"""

avg_arr4 = """select avg((a4_el->>'total_storage_gb')::numeric)
from arr4, 
jsonb_array_elements(data -> 'a1') as a1_el,
jsonb_array_elements(a1_el -> 'a2') as a2_el,
jsonb_array_elements(a2_el -> 'a3') as a3_el,
jsonb_array_elements(a3_el -> 'a4') as a4_el 
where (a4_el @> '{"error_count": %s}')"""

avg_arr8 = """select avg((a8_el->>'total_storage_gb')::numeric)
from arr8, 
jsonb_array_elements(data -> 'a1') as a1_el,
jsonb_array_elements(a1_el -> 'a2') as a2_el,
jsonb_array_elements(a2_el -> 'a3') as a3_el,
jsonb_array_elements(a3_el -> 'a4') as a4_el,
jsonb_array_elements(a4_el -> 'a5') as a5_el,
jsonb_array_elements(a5_el -> 'a6') as a6_el,
jsonb_array_elements(a6_el -> 'a7') as a7_el,
jsonb_array_elements(a7_el -> 'a8') as a8_el 
where (a8_el @> '{"error_count": %s}')"""

avg = {
    1: avg_arr1, 
    2: avg_arr2,
    4: avg_arr4,
    8: avg_arr8,
}


update_storage_arr1 = """update arr1
set data = %s
where data @@ '$.a1[*].error_count == %s'
)"""

update_storage_arr2 = """update arr2
set data = %s
where data @@ '$.a1[*].a2[*].error_count == %s'
)"""

update_storage_arr4 = """update arr4
set data = %s
where data @@ '$.a1[*].a2[*].a3[*].a4[*].error_count == %s'
)"""

update_storage_arr8 = """update arr8
set data = %s
where data @@ '$.a1[*].a2[*].a3[*].a4[*].a5[*].a6[*].a7[*].a8[*].error_count == %s'
)"""

update_storage = {
    1: update_storage_arr1, 
    2: update_storage_arr2,
    4: update_storage_arr4,
    8: update_storage_arr8,
}
