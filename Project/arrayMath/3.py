# 线性代数模块
import numpy as np

a = np.array([3, 4])
b = np.linalg.norm(a)
print(b)
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

c = np.array([1, 0, 1])
# 矩阵和向量之间的乘法
np.dot(b, c)  # array([ 4, 10, 16])
np.dot(c, b.T)  # array([ 4, 10, 16])   b.T 相当于b.transpose  详情可以看1.py

np.trace(b)  # 求矩阵的迹，15  一个n×n矩阵A的主对角线（从左上方至右下方的对角线）上各个元素的总和被称为矩阵A的迹
np.linalg.det(b)  # 求矩阵的行列式值，0
x = np.linalg.matrix_rank(b)  # 求矩阵的秩，2，不满秩，因为行与行之间等差
'''
矩阵秩： 
        | 1,2,1 |
        | 0,3,2 |
        | 0,0,0 |  非0行数就是矩阵的秩'''
print(x)

d = np.array([
    [2, 1],
    [1, 2]
])

'''
对正定矩阵求本征值和本征向量
本征值为u，array([ 3.,  1.])
本征向量构成的二维array为v，
array([[ 0.70710678, -0.70710678],
       [ 0.70710678,  0.70710678]])
是沿着45°方向
eig()是一般情况的本征值分解，对于更常见的对称实数矩阵，
eigh()更快且更稳定，不过输出的值的顺序和eig()是相反的
d = np.array([
    [1, -1, 0],
    [4, -3, 0],
    [-1, 0, -2]
])
'''
u, v = np.linalg.eig(d)

print(u, '\n', v)
# Cholesky分解并重建
l = np.linalg.cholesky(d)

'''
array([[ 2.,  1.],
       [ 1.,  2.]])
'''
x = np.dot(l, l.T)
print(x)
e = np.array([
    [1, 2],
    [3, 4]
])

# 对不镇定矩阵，进行SVD分解并重建
U, s, V = np.linalg.svd(e)

print(U, s, V)
S = np.array([
    [s[0], 0],
    [0, s[1]]
])
print(S)

'''
array([[ 1.,  2.],
       [ 3.,  4.]])
'''
np.dot(U, np.dot(S, V))
