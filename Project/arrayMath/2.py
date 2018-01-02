# 基础数学运算

import numpy as np

# 绝对值
a = np.abs(-1)
print(a)

# sin函数
b = np.sin(np.pi / 2)
print(b)

# tanh逆函数，0.50000107157840523
c = np.arctanh(0.462118)
print(c)

# e为底的指数函数，20.085536923187668
c = np.exp(3)
print(c)

# 2的3次方，8
f = np.power(2, 3)

# 点积，1*3+2*4=11
g = np.dot([1, 2], [3, 4])

# 开方，5
h = np.sqrt(25)

# 求和，10
l = np.sum([1, 2, 3, 4])

# 平均值，5.5
m = np.mean([4, 5, 6, 7])

# 标准差，0.96824583655185426
p = np.std([1, 2, 3, 2, 1, 3, 2, 0])

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [1, 2, 3],
    [1, 2, 3]
])

print('a*b', '\n', a * b)  # 不懂这个同一维度的乘法关系[关系上是每个元素的乘法]

'''
广播机制让计算的表达式保持简洁
d和c的每一行分别进行运算'''

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
d = np.array([2, 2, 2])

print(c, '\n', d)

print(c + d)
print(c - 1)
print(c * d)
