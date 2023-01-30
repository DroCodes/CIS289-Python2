import numpy as np

array_1 = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
array_2 = np.array([[1, 2, 5], [8, 0, 12], [11, 14.5, 18]])

print(array_1)
print(array_1.shape)
print(array_1[0:2, 0:2])
print(array_1 % 2 == 0)
print(array_1 + array_2)
print(array_1 * array_2)
print(np.sum(array_1))
print(np.prod(array_1))
print(np.max(array_1))
print(np.min(array_1))