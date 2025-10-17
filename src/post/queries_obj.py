read_obj1 = """
select data
from obj1 
where data @@ '$.a1[*].error_count == %s'
"""

read_obj2 = """
select data
from obj2
where data @@ '$.a1[*].a2[*].error_count == %s'
"""

read_obj4 = """
select data
from obj4
where data @@ '$.a1[*].a2[*].a3[*].a4[*].error_count == %s'
"""
read_obj8 = """
select data
from obj8
where data @@ '$.a1[*].a2[*].a3[*].a4[*].a5[*].a6[*].a7[*].a8[*].error_count == %s'
"""

read = {
    1: read_obj1, 
    2: read_obj2,
    4: read_obj4,
    8: read_obj8,
}

sort_obj1 = """
select a1_el
from obj1, 
jsonb_objay_elements(data -> 'a1') as a1_el 
where (a1_el @> '{"error_count": %s}')
order by (a1_el ->>'total_storage_gb')::int"""

sort_obj2 = """select a2_el
from obj2, 
jsonb_objay_elements(data -> 'a1') as a1_el,
jsonb_objay_elements(a1_el -> 'a2') as a2_el 
where (a2_el @> '{"error_count": %s}')
order by (a2_el ->>'total_storage_gb')::int"""

sort_obj4 = """select a4_el
from obj4, 
jsonb_objay_elements(data -> 'a1') as a1_el,
jsonb_objay_elements(a1_el -> 'a2') as a2_el,
jsonb_objay_elements(a2_el -> 'a3') as a3_el,
jsonb_objay_elements(a3_el -> 'a4') as a4_el 
where (a4_el @> '{"error_count": %s}')
order by (a4_el ->>'total_storage_gb')::int"""

sort_obj8 = """select a8_el
from obj8, 
jsonb_objay_elements(data -> 'a1') as a1_el,
jsonb_objay_elements(a1_el -> 'a2') as a2_el,
jsonb_objay_elements(a2_el -> 'a3') as a3_el,
jsonb_objay_elements(a3_el -> 'a4') as a4_el,
jsonb_objay_elements(a4_el -> 'a5') as a5_el,
jsonb_objay_elements(a5_el -> 'a6') as a6_el,
jsonb_objay_elements(a6_el -> 'a7') as a7_el,
jsonb_objay_elements(a7_el -> 'a8') as a8_el 
where (a8_el ->> '{"error_count": %s}')
order by (a8_el ->>'total_storage_gb')::int"""

sort = {
    1: sort_obj1, 
    2: sort_obj2,
    4: sort_obj4,
    8: sort_obj8,
}

avg_obj1 = """select avg((a1_el->>'total_storage_gb')::numeric)
from obj1, 
jsonb_objay_elements(data -> 'a1') as a1_el 
where (a1_el @> '{"error_count": %s}')"""

avg_obj2 = """select avg((a2_el->>'total_storage_gb')::numeric)
from obj2, 
jsonb_objay_elements(data -> 'a1') as a1_el 
jsonb_objay_elements(a1_el -> 'a2') as a2_el,
where (a2_el @> '{"error_count": %s}')"""

avg_obj4 = """select avg((a4_el->>'total_storage_gb')::numeric)
from obj4, 
jsonb_objay_elements(data -> 'a1') as a1_el,
jsonb_objay_elements(a1_el -> 'a2') as a2_el,
jsonb_objay_elements(a2_el -> 'a3') as a3_el,
jsonb_objay_elements(a3_el -> 'a4') as a4_el 
where (a4_el @> '{"error_count": %s}')"""

avg_obj8 = """select avg((a8_el->>'total_storage_gb')::numeric)
from obj8, 
jsonb_objay_elements(data -> 'a1') as a1_el,
jsonb_objay_elements(a1_el -> 'a2') as a2_el,
jsonb_objay_elements(a2_el -> 'a3') as a3_el,
jsonb_objay_elements(a3_el -> 'a4') as a4_el,
jsonb_objay_elements(a4_el -> 'a5') as a5_el,
jsonb_objay_elements(a5_el -> 'a6') as a6_el,
jsonb_objay_elements(a6_el -> 'a7') as a7_el,
jsonb_objay_elements(a7_el -> 'a8') as a8_el 
where (a8_el ->> '{"error_count": %s}')"""

avg = {
    1: avg_obj1, 
    2: avg_obj2,
    4: avg_obj4,
    8: avg_obj8,
}


update_storage_obj1 = """update obj1
set data = %s
where exists(
    select 1
    from 
        jsonb_objay_elements(data -> 'a1') as a1_el 
    where (a1_el @> '{"error_count": %s}')
)"""

update_storage_obj2 = """update obj2
set data = %s
where exists(
    select 1
    from 
        jsonb_objay_elements(data -> 'a1') as a1_el,
        jsonb_objay_elements(a1_el -> 'a2') as a2_el
    where (a2_el @> '{"error_count": %s}')
)"""

update_storage_obj4 = """update obj4
set data = %s
where exists(
    select 1
    from 
        jsonb_objay_elements(data -> 'a1') as a1_el,
        jsonb_objay_elements(a1_el -> 'a2') as a2_el,
        jsonb_objay_elements(a2_el -> 'a3') as a3_el,
        jsonb_objay_elements(a3_el -> 'a4') as a4_el 
    where (a4_el @> '{"error_count": %s}')
)"""

update_storage_obj8 = """update obj8
set data = %s
where exists(
    select 1
    from 
        jsonb_objay_elements(data -> 'a1') as a1_el,
        jsonb_objay_elements(a1_el -> 'a2') as a2_el,
        jsonb_objay_elements(a2_el -> 'a3') as a3_el,
        jsonb_objay_elements(a3_el -> 'a4') as a4_el,
        jsonb_objay_elements(a4_el -> 'a5') as a5_el,
        jsonb_objay_elements(a5_el -> 'a6') as a6_el,
        jsonb_objay_elements(a6_el -> 'a7') as a7_el,
        jsonb_objay_elements(a7_el -> 'a8') as a8_el 
    where (a8_el ->> '{"error_count": %s}')
)"""

update_storage = {
    1: update_storage_obj1, 
    2: update_storage_obj2,
    4: update_storage_obj4,
    8: update_storage_obj8,
}


