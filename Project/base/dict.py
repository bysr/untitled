# 字典
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

# 需求：绑定人名和成绩单
# 字典 中括号
d = {'Michael': 95, 'Bob': 75, 1: 85}
print('测试：', d[1])

# 插入值
d['Tex'] = 45
print(d)

# 判断值是否存在
if 'Michael' in d:
    print(True)
else:
    print(False)

# 删除携带返回值
a = d.pop('Tex')
print(a)
print(d)

# set,一组key的集合，但是不存储value
# 所以set中保证不能有重合的数据

s = set([1, 2, 2, 3])
print(s)

# 添加方法
s.add(5)
print(s)

d['key'] = names
print(d)

