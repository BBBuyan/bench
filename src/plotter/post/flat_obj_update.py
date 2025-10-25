import matplotlib.pyplot as plt
import numpy as np

width = 0.15 
x = np.arange(5)
categories = ["flat","1", "2", "4", "8"]

f_read_no                = [451]
f_sort_no                = [444]
f_avg_no                 = [451]
f_update_no              = [541]
f_insert_no              = [3]

f_read_arrow                = [30]
f_sort_arrow                = [20]
f_avg_arrow                 = [32]
f_update_arrow              = [53]
f_insert_arrow              = [15]

f_read_index                = [102]
f_sort_index                = [149]
f_avg_index                 = [155]
f_update_index              = [203]
f_insert_index              = [5]

f_read_path                = [46]
f_sort_path                = [46]
f_avg_path                 = [47]
f_update_path              = [66]
f_insert_path              = [5]

read_path                = f_read_path + [62, 65, 65, 59]
sort_path                = f_sort_path + [60, 64, 32, 31]
avg_path                 = f_avg_path  + [65, 60, 62, 58]
update_path              = f_update_path + [64, 74, 65, 70]
insert_path              = f_insert_path + [5, 4, 6, 6]

read_no                = f_read_no  +[489, 7461, 9225, 10284]
sort_no                = f_sort_no  +[483, 7426, 3267, 10207]
avg_no                 = f_avg_no   +[4167, 8529, 2314, 10227]
update_no              = f_update_no +[668, 1244, 1468, 8845]
insert_no              = f_insert_no +[4, 3, 4, 4]

read_index                = f_read_index  + [193, 265, 376, 709]
sort_index                = f_sort_index  + [219, 328, 340, 213]
avg_index                 = f_avg_index   + [260, 312, 311, 522]
update_index              = f_update_index+ [196, 310, 376, 525]
insert_index              = f_insert_index+ [5, 5, 5, 5]

read_arrow                = f_read_arrow  + [7, 18, 39, 39]
sort_arrow                = f_sort_arrow  + [12, 15, 23, 23]
avg_arrow                 = f_avg_arrow   + [5, 15, 39, 39]
update_arrow              = f_update_arrow+ [33, 32, 46, 49]
insert_arrow              = f_insert_arrow+ [4, 8, 11, 8]

fig, axs = plt.subplots(1,1,constrained_layout=True, sharey=True)
axs.bar(x - 1.5*width   , update_no, width, label='no index')
axs.bar(x - 0.5*width   , update_index, width, label='with GIN')
axs.bar(x + 0.5*width   , update_path, width, label='with jsonb_path_ops')
axs.bar(x + 1.5*width   , update_arrow, width, label='with BTREE')

axs.set_xticks(x, categories)
axs.set_yscale("log")

fig.supxlabel("Depth")

plt.ylabel("Duration / ms (log scale)")
fig.legend(loc="outside upper right", ncol=4)
fig.savefig("./post_figs/flat_obj_update.pdf")
