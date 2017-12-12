from collections import Iterable

# 切片操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])

# 倒数切片
print(L[-2:-1])

print(L[:2])

# tuple同样可以执行
L = (1, 2, 3, 4)
print(L[:2])

# 字符串同样可以切片
a = 'abcdefghigklmnopqrstuvwxyz'
print(a[:5])


# 迭代操作
# dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d.items():
    print(key)

# 判断是否是可迭代对象
print(isinstance('abc', Iterable))

# enumerate函数,找出下标
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


