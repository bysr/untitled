# 读文件
# 方式1
try:
    f = open('C:/Users/wangyawen/Desktop/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 简单方式
with open('__init__.py', 'r') as f:
    print(f.read())

# f = open('C:/Users/wangyawen/Desktop/1513912263(1).jpg', 'rb')
# print(f.read())

# 写文件


with open('C:/Users/wangyawen/Desktop/test.txt', 'w') as f:
    f.write('hello,world,你好')
    


