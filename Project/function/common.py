# 普通函数

# 函数赋值给变量 一种神奇的用法
a = abs  # 变量a 指向abs函数
print(a(-1))


# 定义函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(50))


# 函数的参数
def power(x):
    return x * x


print(power(10))


# 求任意次方,添加默认参数
def power(x, n=3):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))


def add_end(t=[]):
    t.append('END')
    return t


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())


# ['END', 'END', 'END'] 显示结


def add_end(t=None):
    if t is None:
        t = []
    t.append('END')
    return t


print(add_end())
print(add_end())
print(add_end())


# 可变参数传参方式
def calc(*number):
    s = 0
    for n in number:
        s = s + n * n
    return s


# 注意
print(calc(1, 2))
print(calc(*[23, 5]))
print(calc(*(23, 5)))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Michael', 30))
print(person('Mr Li', 35, city='beijing'))
print(person('Mr wen', age=35, city='beijing'))
print(person('Mr wen', age=35, gender='M', city='beijing'))

extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Mr Li', age=20, **extra))


# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:  # 有city参数
        pass
    if 'job' in kw:  # 有job参数
        pass

    print('name:', name, 'age:', age, 'other:', kw)


print(person('Jack', 24, city='Beijing', addr='朝阳', zipcode=123456))


# 命名关键字参数和位置关键字参数区别 * 后面的关键字为命名关键字，前面为位置关键字
def person(name, age, *, city, job):
    print(name, age, city, job)


print(person('Jack', 24, city='Beijing', job='Engineer'))


# 如果函数中有可变参数，后面跟着的命名关键字参数就不在需要一个特殊分隔符*
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# person('Jack', 24, 'Beijing', 'Engineer') 错误原因：Python把这四个参数均认为是位置参数
# 但是person默认只接受两个位置参数

# 参数组合
# 注意参数定义的顺序是：必选参数 默认参数 可变参数 命名关键字参数和关键字参数
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict

# 位置参数、位置参数、默认参数、可变参数、关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


# 位置参数、位置参数、默认参数、命名关键字参数、关键字参数
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


print(f1(1, 2))
print(f1(1, 2, 3))
print(f1(1, 2, *(1, 2, 3)))
print(f1(1, 2, 2, *(1, 2, 3), x=99))
print(f2(1, 1, 2, d=2, y=3, x='1'))
