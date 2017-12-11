# 条件判断
age = 20
if age > 16:
    print('your age is', age)
    print('adult')
elif age > 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')


# if 简写
x = 10
if x:
    print(True)

x = 0
if x:
    print(True)   # 不执行，只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False

# input输入
birth = input('birth:')
# int类型
birth = int(birth)

if birth < 2000:
    print('00前')
else:
    print('00后')



