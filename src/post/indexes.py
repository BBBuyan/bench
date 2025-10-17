flat_index = "create index idx_flat_error_count on flat using GIN (data)"
flat_index_drop = "drop index if exists idx_flat_error_count"

obj1_index = "create index idx_obj1_error_count on obj1 using GIN (data)"
obj2_index = "create index idx_obj2_error_count on obj2 using GIN (data)"
obj4_index = "create index idx_obj4_error_count on obj4 using GIN (data)"
obj8_index = "create index idx_obj8_error_count on obj8 using GIN (data)"

obj1_index_drop = "drop index if exists idx_obj1_error_count"
obj2_index_drop = "drop index if exists idx_obj2_error_count"
obj4_index_drop = "drop index if exists idx_obj4_error_count"
obj8_index_drop = "drop index if exists idx_obj8_error_count"

obj_indexes = {
    1: obj1_index,
    2: obj2_index,
    4: obj4_index,
    8: obj8_index,
}

obj_indexes_drop = {
    1: obj1_index_drop,
    2: obj2_index_drop,
    4: obj4_index_drop,
    8: obj8_index_drop,
}

arr1_index = "create index idx_arr1_error_count on arr1 using GIN (data)"
arr2_index = "create index idx_arr2_error_count on arr2 using GIN (data)"
arr4_index = "create index idx_arr4_error_count on arr4 using GIN (data)"
arr8_index = "create index idx_arr8_error_count on arr8 using GIN (data)"

arr1_index_drop = "drop index if exists idx_arr1_error_count"
arr2_index_drop = "drop index if exists idx_arr2_error_count"
arr4_index_drop = "drop index if exists idx_arr4_error_count"
arr8_index_drop = "drop index if exists idx_arr8_error_count"

arr_indexes = {
    1: arr1_index,
    2: arr2_index,
    4: arr4_index,
    8: arr8_index,
}

arr_indexes_drop = {
    1: arr1_index_drop,
    2: arr2_index_drop,
    4: arr4_index_drop,
    8: arr8_index_drop,
}
