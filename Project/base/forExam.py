# 循环
names = ['Micheal', 'Bob', 'Tracy']

# 获取每一个人
for name in names:
    print(name)

# 计算从1到100的值
num = 0
Sum = 0
while num <= 100:
    Sum = Sum + num
    num = num + 1
print(Sum)

# range 可以生成一个有序的数列
nums = list(range(101))
print(nums)

sums = 0
for n in range(101):
    sums += n
print(sums)
