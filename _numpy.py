import numpy as np

li1 = [1, 2, 3]
li2 = [4, 5, 6]
print(np.array(li1))
print(np.array([li1, li2]))

print(np.random.rand())
print(np.random.rand(2))
print(np.random.rand(5, 2))

print(np.zeros(3))
print(np.zeros((2, 3)))

print(np.ones(3))
print(np.ones((2, 3)))

arr1 = np.arange(1, 20, 2) #arrange 아님 # 1부터 9까지 2씩 증가
print(arr1)
print(arr1.reshape(2, 5))

arr2 = np.array([[1, 6, 5], [3, 2, 4]])
arr2.sort(0) # 0 열 1 행
print(arr2)
arr2 = np.array([[1, 6, 5], [3, 2, 4]])
arr2.sort(1) # 0 열 1 행
print(arr2)

arr2 = np.array([[1, 6, 5], [3, 2, 4]])

print(arr2.min())
print(arr2.min(axis=0))
print(arr2.min(axis=1))

print(arr2.max())
print(arr2.max(axis=0))
print(arr2.max(axis=1))

print(arr2.sum())

print(arr2 > 3)
print((arr2 > 3).sum())

print(np.where(arr2 > 3, '3보다 큼', '3보다 작거나 같음'))

'''
[1 2 3]
[[1 2 3]
 [4 5 6]]
0.32555165667360964
[0.87404862 0.75242017]
[[0.81502002 0.36392253]
 [0.32637375 0.19618939]
 [0.50250085 0.40965038]
 [0.25724184 0.20522974]
 [0.58306905 0.19796745]]
[0. 0. 0.]
[[0. 0. 0.]
 [0. 0. 0.]]
[1. 1. 1.]
[[1. 1. 1.]
 [1. 1. 1.]]
[ 1  3  5  7  9 11 13 15 17 19]
[[ 1  3  5  7  9]
 [11 13 15 17 19]]
[[1 2 4]
 [3 6 5]]
[[1 5 6]
 [2 3 4]]
1
[1 2 4]
[1 2]
6
[3 6 5]
[6 4]
21
[[False  True  True]
 [False False  True]]
3
[['3보다 작거나 같음' '3보다 큼' '3보다 큼']
 ['3보다 작거나 같음' '3보다 작거나 같음' '3보다 큼']]
'''