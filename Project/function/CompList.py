# 列表生成式

import os  # 导入os模块，模块的概念后面讲到


L = ['Java', 'C', 'Swift', 'Python', 123]

# 筛选出字符串以及字母小写显示
print([s.lower() for s in L if isinstance(s, str)])


print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录


# 生成器
g = (s.lower() for s in L if isinstance(s, str))
print(g)
print(next(g))  # java
print(next(g))  # c
print(next(g))  # swift
print('------------------------------')
for n in g:
    print(n)


# 斐波那契数列
def fib(mx):
    n, a, b = 0, 0, 1
    while n < mx:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


o = fib(6)
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))
# print(next(o))   stopIteration: done


# 小结
#
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的

