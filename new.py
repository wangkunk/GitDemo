import numpy as np

# arr1 = np.array([2,3,4])
#
# print(arr1)
# print(arr1.dtype)


arr4 = np.arange(10)

arr4[5:8] = 10

print(arr4)

arr_slice = arr4[5:8].copy()

arr_slice[:] = 15

print(arr_slice)
print(arr4)
