#!/usr/bin/env python3

# import sys
# import numpy as np
#
# # data = np.loadtxt(sys.stdin).T.reshape(-1, 3).T
# data = np.loadtxt('day3input.txt').T.reshape(-1, 3).T
# data.sort(axis=0)
# print(np.sum(sum(data[:2]) > data[2]))
#
#



import numpy as np

in_ = np.loadtxt('day3input.txt')

def find_triangles(arr):
    arr.sort(axis=1)
    return sum(np.sum(arr[:, :2], axis=1) > arr[:, 2])

print(find_triangles(in_.copy()))
print(find_triangles(in_.T.reshape(-1, 3)))
