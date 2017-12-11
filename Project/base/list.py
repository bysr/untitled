# list 有序集合
# 数据类型可任意
classmate = ['Michael', 5, 'Tracy']


print(classmate)
print(len(classmate))
print(classmate[1])

# 倒序
print(classmate[-1])

# 添加元素
classmate.append('Jack')

# 插入元素
classmate.insert(1, 'Mr Wang')

# 删除末尾元素
classmate.pop()

# 删除指定位置元素
classmate.pop(1)

# 替换元素
classmate[0] = 'Mr First'
print(classmate)

# 集合中可包含其他集合
s = ['hello', 20, classmate]
print(s)

# 拿到classmate第一个元素
print(s[2][0])


# tuple 元组
# 有序列表，一旦初始化无法修改，可当成对饮的指针不可变
mate = (1, 5, 'Tracy')
print(mate)

# 定义空元组集合
mate = ()
print(mate)

# 一个元素,需要添加,解除歧义
mate = (1, )
print(mate)



