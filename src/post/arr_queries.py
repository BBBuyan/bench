read_arr1 = """select a1_elem
from arr1, 
jsonb_array_elements(data -> a1) as a1_el 
where (a1_el ->> 'model_number')::int = %s"""

read_arr2 = """select a2_el
from arr2, 
jsonb_array_elements(data -> a1) as a1_el 
jsonb_array_elements(a1_el -> a2) as a2_el 
where (a2_el ->> 'model_number')::int = %s"""

read_arr4 = """select a4_el
from arr4, 
jsonb_array_elements(data -> a1) as a1_el 
jsonb_array_elements(a1_el -> a2) as a2_el 
jsonb_array_elements(a2_el -> a3) as a3_el 
jsonb_array_elements(a3_el -> a4) as a4_el 
where (a4_el ->> 'model_number')::int = %s"""

read_arr8 = """select a8_elem
from arr8, 
jsonb_array_elements(data -> a1) as a1_el 
jsonb_array_elements(a1_el -> a2) as a2_el 
jsonb_array_elements(a2_el -> a3) as a3_el 
jsonb_array_elements(a3_el -> a4) as a4_el 
jsonb_array_elements(a4_el -> a5) as a5_el 
jsonb_array_elements(a5_el -> a6) as a6_el 
jsonb_array_elements(a6_el -> a7) as a7_el 
jsonb_array_elements(a7_el -> a8) as a8_el 
where (a8_el ->> 'model_number')::int = %s"""

read = {
    1: read_arr1, 
    2: read_arr2,
    4: read_arr4,
    8: read_arr8,
}
