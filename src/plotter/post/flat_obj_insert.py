import matplotlib.pyplot as plt
import numpy as np

width = 0.15 
x = np.arange(5)
categories = ["flat","1", "2", "4", "8"]

f_insert_no              = [3]
f_insert_arrow           = [9]
f_insert_index           = [5]
f_insert_path            = [5]

insert_no              =    f_insert_no+[4, 3, 4, 4]
insert_index              = f_insert_index+ [5, 5, 5, 5]
insert_arrow              = f_insert_arrow+ [4, 8, 11, 8]
insert_path              =  f_insert_path + [5, 4, 6, 6]


fig, axs = plt.subplots(1,1,constrained_layout=True, sharey=True)
axs.bar(x - 1.5*width   , insert_no, width, label='no index')
axs.bar(x - 0.5*width   , insert_index, width, label='with GIN')
axs.bar(x + 0.5*width   , insert_path, width, label='with jsonb_path_ops')
axs.bar(x + 1.5*width   , insert_arrow, width, label='with BTREE')

axs.set_xticks(x, categories)
plt.ylabel("Duration / ms")

fig.supxlabel("Depth")
fig.legend(loc="outside upper right", ncol=4)
fig.savefig("./post_figs/flat_obj_insert.pdf")
