flat_index_arrow = "create index idx_flat_arrow on flat using btree (((data ->> 'error_count')::int))"
flat_index_arrow_drop = "drop index idx_flat_arrow"

obj1_index_arrow = "create index idx_obj1_arrow on obj1 using btree (((data->'l1'->>'error_count')::int))"
obj2_index_arrow = "create index idx_obj2_arrow on obj2 using btree (((data->'l1'->'l2'->>'error_count')::int))"
obj4_index_arrow = "create index idx_obj4_arrow on obj4 using btree (((data->'l1'->'l2'->'l3'->'l4'->>'error_count')::int))"
obj8_index_arrow = "create index idx_obj8_arrow on obj8 using btree (((data->'l1'->'l2'->'l3'->'l4'->'l5'->'l6'->'l7'->'l8'->>'error_count')::int))"

obj1_index_arrow_drop = "drop index if exists idx_obj1_arrow"
obj2_index_arrow_drop = "drop index if exists idx_obj2_arrow"
obj4_index_arrow_drop = "drop index if exists idx_obj4_arrow"
obj8_index_arrow_drop = "drop index if exists idx_obj8_arrow"

obj_indexes_arrow = {
    1: obj1_index_arrow,
    2: obj2_index_arrow,
    4: obj4_index_arrow,
    8: obj8_index_arrow,
}

obj_indexes_arrow_drop = {
    1: obj1_index_arrow_drop,
    2: obj2_index_arrow_drop,
    4: obj4_index_arrow_drop,
    8: obj8_index_arrow_drop,
}

