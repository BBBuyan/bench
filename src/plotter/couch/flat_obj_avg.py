import matplotlib.pyplot as plt
import numpy as np

fa_avg_only = [8]
fa_avg_after_update = [137]
fa_avg_after_insert = [94]
f_a_avg = fa_avg_only + fa_avg_after_update + fa_avg_after_insert

fs_avg_only = [10]
fs_avg_after_update = [84]
fs_avg_after_insert = [71]

f_s_avg = fs_avg_only + fs_avg_after_update + fs_avg_after_insert

a_avg_only = [7,7,7,7]
a_avg_after_update = [138,132,131,142]
a_avg_after_insert = [91,97,95,98]

s_avg_only = [10,9,9,9]
s_avg_after_update = [85,88,88,91]
s_avg_after_insert = [70,69,65,70]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

xf = np.arange(3)
xfl=xf-w/2
xfr=xf+w/2

fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xfl, f_a_avg, width=w, label="alone")
bar02 = axs[0].bar(xfr, f_s_avg, width=w, label="sharded")

bar11 = axs[1].bar(xl, a_avg_only, width=w, label="alone")
bar12 = axs[1].bar(xr, s_avg_only, width=w, label="sharded")

bar21 = axs[2].bar(xl, a_avg_after_update, width=w, label="alone")
bar22 = axs[2].bar(xr, s_avg_after_update, width=w, label="sharded")

bar31 = axs[3].bar(xl, a_avg_after_insert, width=w, label="alone")
bar32 = axs[3].bar(xr, s_avg_after_insert, width=w, label="sharded")

levels = [1,2,4,8]

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[1].set_xticks(x,levels)
axs[2].set_xticks(x,levels)
axs[3].set_xticks(x,levels)

fig.savefig("./couch_figs/flat_obj_avg.pdf", bbox_inches="tight")
