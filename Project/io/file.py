import os
import shutil

print(os.name)

# print(os.uname())  window上不存在该函数

print(os.environ)
print(os.environ.get("PATH"))
print(os.path.abspath('.'))  # 当前文件的绝对路劲
print(os.path.join('C:/', 'testdir'))
os.mkdir('C:/testdir')  # 创建一个目录
os.rmdir("C:/testdir")  # 删除一个目录

# 分隔符；
# os.path.join()
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
path = '/Users/michael/testdir/file.txt'
# 文件名称
p_name = os.path.split(path)
print(p_name)
# 扩展名
e_name = os.path.splitext(path)
print(e_name)
# 重命名，该函数需要文件真实存在
# os.rename('Serialization.py', 'pickling.py')
# 删除文件
# os.remove('C:\\test.py')

# 复制文件
# shutil.copyfile('test.py', 'test.txt')
# 罗列当前目录文件
m = os.listdir('.')
print(m)
#  当前目录文件夹
mdir = [x for x in os.listdir('.') if os.path.isdir(x)]
# 当期目录文件
mpath = [x for x in os.listdir('.') if os.path.isfile(x)]
# 当前目录py文件
mpy = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print('文件夹=>', mdir)
print('所有文件=>', mpath)

print('py文件=>', mpy)
