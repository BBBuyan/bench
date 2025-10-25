import matplotlib.pyplot as plt
import numpy as np

width = 0.15 
x = np.arange(4)
categories = ["1", "2", "4", "8"]

update_no              = [58, 141, 485, 13508]
update_index              = [3, 3, 486, 22413]
update_path              = [4, 10, 559, 11521]

plt.bar(x - width ,update_no, width, label='no index')
plt.bar(x           ,update_index, width, label='with GIN')
plt.bar(x + width ,update_path, width, label='with jsonb_path_ops')

plt.yscale("log")
plt.xticks(x, categories)
plt.xlabel("Depth")
plt.ylabel("Duration / ms (log scale)")
plt.legend()
plt.tight_layout()

plt.savefig("./post_figs/arr_update.pdf")
