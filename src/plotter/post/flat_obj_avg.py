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

read_no                =f_read_no  +[489, 7461, 9225, 10284]
sort_no                =f_sort_no  +[483, 7426, 3267, 10207]
avg_no                 =f_avg_no   +[4167, 8529, 2314, 10227]
update_no              =f_update_no+[668, 8263, 1468, 8845]
insert_no              =f_insert_no+[4, 3, 4, 4]

read_index                =f_read_index  + [193, 265, 376, 709]
sort_index                =f_sort_index  + [219, 328, 340, 213]
avg_index                 =f_avg_index   + [260, 312, 311, 522]
update_index              =f_update_index+ [1155, 270, 343, 536]
insert_index              =f_insert_index+ [5, 5, 5, 5]

read_arrow                =f_read_arrow  + [7, 18, 39, 39]
sort_arrow                =f_sort_arrow  + [12, 15, 23, 23]
avg_arrow                 =f_avg_arrow   + [5, 15, 39, 39]
update_arrow              =f_update_arrow+ [33, 32, 46, 49]
insert_arrow              =f_insert_arrow+ [4, 8, 11, 8]


plt.bar(x - width   , avg_no, width, label='no index')
plt.bar(x           , avg_index, width, label='with index GIN')
plt.bar(x + width   , avg_arrow, width, label='with index BTREE')

plt.yscale("log")
plt.xticks(x, categories)
plt.xlabel("Depth")
plt.ylabel("Duration / ms (log scale)")

plt.legend()
plt.tight_layout()
plt.savefig("./post_figs/flat_obj_avg.pdf")
