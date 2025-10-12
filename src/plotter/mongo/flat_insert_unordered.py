import matplotlib.pyplot as plt
import numpy as np

alone_flat_no_index_small = [108]
alone_flat_no_index_big = [1164]
alone_flat_with_index_small = [172]
alone_flat_with_index_big = [1573]

sharded_flat_no_index_small = [211]
sharded_flat_no_index_big = [2565]
sharded_flat_with_index_small = [226]
sharded_flat_with_index_big = [3179]

o_alone_flat_no_index_small = [153]
o_alone_flat_with_index_small = [145]
o_alone_flat_no_index_big = [1337]
o_alone_flat_with_index_big = [1781]

o_sharded_flat_no_index_small = [9946]
o_sharded_flat_with_index_small = [10489]

o_sharded_flat_no_index_big = [118653]
o_sharded_flat_with_index_big = [119857]

fig, axs = plt.subplots(1,2, sharey=True, constrained_layout=True)

x = np.arange(1)
width = 0.25
xl = x - width/2
xr = x + width/2

axs[0].bar(xl, alone_flat_no_index_small)
axs[0].bar(xr, o_alone_flat_no_index_small)

axs[1].bar(xl, sharded_flat_no_index_small)
axs[1].bar(xr, o_sharded_flat_no_index_small)

# fig.savefig("./mongo_figs/flat_ordered.pdf")
plt.show()
