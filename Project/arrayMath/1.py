# numpy 基本类型(array)

import numpy as np

a = [1, 2, 3, 4]  #
b = np.array(a)  # array([1, 2, 3, 4])
type(b)  # <type 'numpy.ndarray'>

b.shape  # (4,)
b.argmax()  # 3
b.max()  # 4
b.mean()  # 2.5

c = [[1, 2], [3, 4]]  # 二维列表
d = np.array(c)  # 二维numpy数组
d.shape  # (2, 2)
d.size  # 4

print('d', d)
print(d.max(axis=0))  # 找维度0，也就是最后一个维度上的最大值，array([3, 4])
print(d.max(axis=1))  # 找维度1，也就是倒数第二个维度上的最大值，array([2, 4])
print(d.mean(axis=0))  # 找维度0，也就是第一个维度上的均值，array([ 2.,  3.])
print(d.mean(axis=1))  # 找维度0，也就是第一个维度上的均值，array([ 1.5,  3.5])
print(d.flatten())  # 展开一个numpy数组为1维数组，array([1, 2, 3, 4])
print(np.ravel(c))  # 展开一个可以解析的结构为1维数组，array([1, 2, 3, 4])

# 3x3的浮点型2维数组，并且初始化所有元素值为1
e = np.ones((3, 3), dtype=np.float)

# 创建一个一维数组，元素值是把3重复4次，array([3, 3, 3, 3])
f = np.repeat(3, 4)
print('f', f)

# 2x2x3的无符号8位整型3维数组，并且初始化所有元素值为0
g = np.zeros((2, 2, 3), dtype=np.uint8)
g.shape  # (2, 2, 3)
h = g.astype(np.float)  # 用另一种类型表示

l = np.arange(10)  # 类似range，array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.linspace(0, 6, 5)  # 等差数列，0到6之间5个取值，array([ 0., 1.5, 3., 4.5, 6.])

p = np.array(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
)

print('...', p.max(axis=0))
print('....', p.max(axis=1))

np.save('p', p)  # 保存到文件
q = np.load('p.npy')  # 从文件读取
# print(q)


'''
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
'''
a = np.arange(24).reshape((2, 3, 4))  # 转化为2个3*4的矩阵,即矩阵的转置
print(a)
b = a[1][1][1]  # 17
print(b)

c = a[:, 2, :]  # 第3行所有
print(c)
'''用:表示当前维度上所有下标
array([[ 8,  9, 10, 11],
       [20, 21, 22, 23]])
'''
c = a[:, :, 1]  # 2列所有
print(c)
'''
[[ 1  5  9]
 [13 17 21]]'''

e = a[..., 1]
print(e)
'''...表示没有明确指出维度
[[ 1  5  9]
 [13 17 21]]'''

f = a[:, 1:, 1:3]  # a[:, 1:, 1:-1] 结果一样  # 三个变量 ： 1.切片操作 2. 第2行以后的数据 3.第二行和第四行数据
print(a)
print(f)
f = a[:, 1:, 1:-1]
print(f)
''' [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
[[[ 5  6]
  [ 9 10]]

 [[17 18]
  [21 22]]]
[[[ 5  6]
  [ 9 10]]

 [[17 18]
  [21 22]]]'''

# 平均分成三份
g = np.split(np.arange(9), 3)
print(g)
'''[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]'''
# 按照下标位置划分
h = np.split(np.arange(9), [2, -3])
print(h)
'''[array([0, 1]), array([2, 3, 4, 5]), array([6, 7, 8])]
01 //2345 //678

'''
l0 = np.arange(6).reshape((2, 3))  # 2*3 矩阵
l1 = np.arange(6, 12).reshape((2, 3))
print(l0, '\n', l1)
'''[[0 1 2]
 [3 4 5]] 
 [[ 6  7  8]
 [ 9 10 11]]'''
m = np.vstack((l0, l1))  # 纵轴拼接
p = np.hstack((l0, l1))  # 横轴拼接
print(m, '\n', p)

# 或者通过下面的方式实现
q = np.concatenate((l0, l1))  # 纵轴拼接 或者axis=0
r = np.concatenate((l0, l1), axis=-1)  # 横轴拼接
print(q)
print(r)

# 不是拼接 而是增加一个维度
s = np.stack((l0, l1))
print(s)
'''[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
 
 
[[ 0  1  2  6  7  8]
 [ 3  4  5  9 10 11]]

 
 [[[ 0  1  2]
  [ 3  4  5]]

 [[ 6  7  8]
  [ 9 10 11]]]'''
# 按指定轴进行装置
t = s.transpose((2, 1, 0))  # 不太明白 ？？？？？？？？？？？？？？？？？？？？？？？
print('指定轴转置', '\n', t)

u = a[0].transpose()  # 矩阵转置 行变列
print(a[0])
print(u)

v = np.rot90(u, 3)  # 逆时针旋转90  旋转三次
print(v)
'''[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
 
[[ 3  2  1  0]
 [ 7  6  5  4]
 [11 10  9  8]]'''

w = np.fliplr(u)
print(w)  # 水平左右翻转

x = np.flipud(u)
print(x)  # 水平上下翻转

'''[[ 8  4  0]
 [ 9  5  1]
 [10  6  2]
 [11  7  3]]
[[ 3  7 11]
 [ 2  6 10]
 [ 1  5  9]
 [ 0  4  8]]'''

y = np.roll(u, 1)  # 按照一维顺序滚动位移 不太明白？？？？？？？？？？？？？？？
z = np.roll(u, 1, axis=-1)
z1 = np.roll(u, 1, axis=1)  # 指定轴滚动位移 z1=z2
z2 = np.roll(u, 1, axis=0)  # 纵向移动
print(u)
print(y)
print(z2)
