depth_list = [1,2,4,8]

flat_vol_paths = ["total_volume_bytes"]
flat_num_paths = ["number_of_records"]
flat_sub_paths = ["subscribers"]
flat_app_paths = ["app"]

arr_vol_path_1 = "a1.total_volume_bytes"
arr_vol_path_2 = "a1.a2.total_volume_bytes"
arr_vol_path_4 = "a1.a2.a3.a4.total_volume_bytes"
arr_vol_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8.total_volume_bytes"
arr_vol_paths = [arr_vol_path_1, arr_vol_path_2, arr_vol_path_4, arr_vol_path_8]

arr_num_path_1 = "a1.number_of_records"
arr_num_path_2 = "a1.a2.number_of_records"
arr_num_path_4 = "a1.a2.a3.a4.number_of_records"
arr_num_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8.number_of_records"
arr_num_paths = [arr_num_path_1, arr_num_path_2, arr_num_path_4, arr_num_path_8]

arr_sub_path_1 = "a1.subscribers"
arr_sub_path_2 = "a1.a2.subscribers"
arr_sub_path_4 = "a1.a2.a3.a4.subscribers"
arr_sub_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8.subscribers"
arr_sub_paths: list[str] = [arr_sub_path_1, arr_sub_path_2, arr_sub_path_4, arr_sub_path_8]

arr_app_path_1 = "a1.app"
arr_app_path_2 = "a1.a2.app"
arr_app_path_4 = "a1.a2.a3.a4.app"
arr_app_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8.app"
arr_app_paths: list[str] = [arr_app_path_1, arr_app_path_2, arr_app_path_4, arr_app_path_8]

arr_unwind_path_1 = "a1"
arr_unwind_path_2 = "a1.a2"
arr_unwind_path_4 = "a1.a2.a3.a4"
arr_unwind_path_8 = "a1.a2.a3.a4.a5.a6.a7.a8"
arr_unwind_paths = [arr_unwind_path_1, arr_unwind_path_2, arr_unwind_path_4, arr_unwind_path_8]

obj_vol_path_1 = "l1.total_volume_bytes"
obj_vol_path_2 = "l1.l2.total_volume_bytes"
obj_vol_path_4 = "l1.l2.l3.l4.total_volume_bytes"
obj_vol_path_8 = "l1.l2.l3.l4.l5.l6.l7.l8.total_volume_bytes"
obj_vol_paths = [obj_vol_path_1, obj_vol_path_2, obj_vol_path_4, obj_vol_path_8]

obj_num_path_1 = "l1.number_of_records"
obj_num_path_2 = "l1.l2.number_of_records"
obj_num_path_4 = "l1.l2.l3.l4.number_of_records"
obj_num_path_8 = "l1.l2.l3.l4.l5.l6.l7.l8.number_of_records"
obj_num_paths = [obj_num_path_1, obj_num_path_2, obj_num_path_4, obj_num_path_8]

obj_sub_path_1 = "l1.subscribers"
obj_sub_path_2 = "l1.l2.subscribers"
obj_sub_path_4 = "l1.l2.l3.l4.subscribers"
obj_sub_path_8 = "l1.l2.l3.l4.l5.l6.l7.l8.subscribers"
obj_sub_paths: list[str] = [obj_sub_path_1, obj_sub_path_2, obj_sub_path_4, obj_sub_path_8]

obj_app_path_1 = "l1.app"
obj_app_path_2 = "l1.l2.app"
obj_app_path_4 = "l1.l2.l3.l4.app"
obj_app_path_8 = "l1.l2.l3.l4.l5.l6.l7.l8.app"
obj_app_paths: list[str] = [obj_app_path_1, obj_app_path_2, obj_app_path_4, obj_app_path_8]

