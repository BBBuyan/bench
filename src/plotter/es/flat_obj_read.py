import matplotlib.pyplot as plt
import numpy as np

alone_flat_read                 = [10]
alone_flat_avg                  = [4]
alone_flat_group                = [14]
alone_flat_info                 = [3]
alone_flat_description          = [3]

alone_obj_read             = alone_flat_read + [8, 7, 8, 8]
alone_obj_avg              = alone_flat_avg + [3, 3, 3, 3]
alone_obj_group            = alone_flat_group + [12, 13, 12, 13]
alone_obj_info             = alone_flat_info + [3, 3, 2, 3]
alone_obj_description      = alone_flat_description + [3, 3, 3, 3]

s1_flat_read            = [6]
s1_flat_avg             = [3]
s1_flat_group           = [14]
s1_flat_info            = [3]
s1_flat_description     = [3]

s1_obj_read           = s1_flat_read + [11, 8, 9, 6]
s1_obj_avg            = s1_flat_avg + [3, 3, 3, 3]
s1_obj_group          = s1_flat_group + [16, 14, 17, 13]
s1_obj_info           = s1_flat_info + [3, 4, 3, 3]
s1_obj_description    = s1_flat_description + [3, 4, 4, 3]

s3_flat_read                   = [11]
s3_flat_avg                            = [5]
s3_flat_group                          = [13]
s3_flat_info                           = [7]
s3_flat_description                    = [7]

s3_obj_read         =s3_flat_read       + [11, 10, 11, 12]
s3_obj_avg          =s3_flat_avg        + [5, 5, 4, 4]
s3_obj_group        =s3_flat_group      + [11, 11, 10, 11]
s3_obj_info         =s3_flat_info       + [4, 5, 4, 4]
s3_obj_description  =s3_flat_description +[4, 5, 5, 5]

s5_flat_read                   = [13]
s5_flat_avg                            = [5]
s5_flat_group                          = [11]
s5_flat_info                           = [4]
s5_flat_description                    = [6]

s5_obj_read                   = s5_flat_read                +   [13, 13, 17, 13]
s5_obj_avg                    = s5_flat_avg                 +   [6, 6, 5, 6]
s5_obj_group                  = s5_flat_group               +   [14, 12, 12, 13]
s5_obj_info                   = s5_flat_info                +   [7, 7, 7, 7]
s5_obj_description            = s5_flat_description         +   [7, 8, 8, 6]

s8_flat_read                   = [9]
s8_flat_avg                            = [5]
s8_flat_group                          = [10]
s8_flat_info                           = [5]
s8_flat_description                    = [5]

s8_obj_read                   =        s8_flat_read        + [9, 9, 10, 7]
s8_obj_avg                            =s8_flat_avg         + [4, 4, 4, 4]
s8_obj_group                          =s8_flat_group       + [9, 10, 10, 11]
s8_obj_info                           =s8_flat_info        + [6, 5, 5, 5]
s8_obj_description                    =s8_flat_description + [4, 5, 5, 5]

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

# fig, axs = plt.subplots(1,5, sharey=True, constrained_layout=True, figsize=(8,4))
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
plt.savefig("test.pdf")

