import matplotlib.pyplot as plt
import numpy as np

width = 0.15 
x = np.arange(4)
categories = ["1", "2", "4", "8"]

insert_no              = [7, 13, 42, 756]
insert_index              = [13, 17, 70, 1358]
insert_path              =[8, 20, 62, 1527]

plt.bar(x - width,insert_no, width, label='no index')
plt.bar(x ,insert_index, width, label='with GIN')
plt.bar(x + width,insert_path, width, label='with jsonb_path_ops')

plt.yscale("log")
plt.xticks(x, categories)
plt.xlabel("Depth")
plt.ylabel("Duration / ms (log scale)")
plt.legend()
plt.tight_layout()

plt.savefig("./post_figs/arr_insert.pdf")
