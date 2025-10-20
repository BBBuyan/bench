flat_index = "create index idx_flat_path_ops on flat using GIN (data json_path_ops)"
flat_index_drop = "drop index if exists idx_flat_path_ops"

obj1_index = "create index idx_obj1_path_ops on obj1 using GIN (data json_path_ops)"
obj2_index = "create index idx_obj2_path_ops on obj2 using GIN (data json_path_ops)"
obj4_index = "create index idx_obj4_path_ops on obj4 using GIN (data json_path_ops)"
obj8_index = "create index idx_obj8_path_ops on obj8 using GIN (data json_path_ops)"

obj1_index_drop = "drop index if exists idx_obj1_path_ops"
obj2_index_drop = "drop index if exists idx_obj2_path_ops"
obj4_index_drop = "drop index if exists idx_obj4_path_ops"
obj8_index_drop = "drop index if exists idx_obj8_path_ops"

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

arr1_index = "create index idx_arr1_path_ops on arr1 using GIN (data json_path_ops)"
arr2_index = "create index idx_arr2_path_ops on arr2 using GIN (data json_path_ops)"
arr4_index = "create index idx_arr4_path_ops on arr4 using GIN (data json_path_ops)"
arr8_index = "create index idx_arr8_path_ops on arr8 using GIN (data json_path_ops)"

arr1_index_drop = "drop index if exists idx_arr1_path_ops"
arr2_index_drop = "drop index if exists idx_arr2_path_ops"
arr4_index_drop = "drop index if exists idx_arr4_path_ops"
arr8_index_drop = "drop index if exists idx_arr8_path_ops"

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

