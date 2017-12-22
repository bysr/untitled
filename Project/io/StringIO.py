# 内存中读写
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 读取StringIO，写一个初始化StringIO，然后和文件读写一样

f = StringIO('你好\n你是\n小王')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
