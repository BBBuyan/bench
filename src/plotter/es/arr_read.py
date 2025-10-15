import matplotlib.pyplot as plt
import numpy as np

alone_arr_read                   =      [3, 5, 9, 57]
alone_arr_avg                        =  [3, 2, 2, 5]
alone_arr_group                      =  [4, 3, 10, 63]
alone_arr_info                       =  [3, 3, 5, 58]
alone_arr_description                =  [3, 3, 6, 62]

s1_arr_read                   =         [6, 8, 15, 76]
s1_arr_avg                            = [4, 4, 4, 6]
s1_arr_group                          = [7, 8, 16, 77]
s1_arr_info                           = [3, 4, 10, 73]
s1_arr_description                    = [4, 4, 7, 75]

s3_arr_read                   =         [5, 6, 10, 74]
s3_arr_avg                            = [4, 4, 4, 6]
s3_arr_group                          = [6, 7, 12, 88]
s3_arr_info                           = [5, 6, 11, 52]
s3_arr_description                    = [5, 6, 9, 58]

s5_arr_read                   =         [3, 4, 9, 52]
s5_arr_avg                            = [3, 3, 4, 4]
s5_arr_group                          = [5, 6, 9, 58]
s5_arr_info                           = [5, 4, 7, 53]
s5_arr_description                    = [4, 5, 6, 61]

s8_arr_read                   =         [4, 5, 10, 55]
s8_arr_avg                            = [4, 4, 4, 6]
s8_arr_group                          = [6, 6, 11, 54]
s8_arr_info                           = [5, 6, 10, 54]
s8_arr_description                    = [5, 6, 8, 62]

width = 0.15 
x = np.arange(4)
categories = ["1", "3", "5", "8"]

# Plot bars side-by-side
plt.bar(x - 2*width, alone_arr_read, width, label='alone')
plt.bar(x - width,   s1_arr_read, width, label='s = 1')
plt.bar(x,           s3_arr_read, width, label='s = 3')
plt.bar(x + width,   s5_arr_read, width, label='s = 5')
plt.bar(x + 2*width, s8_arr_read, width, label='s = 8')

plt.xticks(x, categories)
plt.title("Read Nested Arrays")
plt.xlabel("Depth")
plt.ylabel("Duration / ms")
plt.legend()
plt.tight_layout()
plt.savefig("arr_read.pdf")

