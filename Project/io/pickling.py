# 序列化
# 定义：变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
import pickle

d = dict(name='Bob', age=20, score=88)
a = pickle.dumps(d)
print(a)

# 序列化数据保存到test.txt文件中
f = open('test.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化，拿到数据
f = open('test.txt', 'rb')
d = pickle.load(f)
f.close()
print('反序列化数据==>', d)


