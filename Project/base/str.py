# 末尾换行
print('1024*45=', 1024 * 45)

# 转译符
print('I\'m OK')
print('I am \n Y')
print('\\\n\\')  # \\表示\,\n 换行

# 多行表示
print('''你是谁
    握手哈岁哦
    ha''')

# r用法  raw 字符串不需要转译
print(r'''hello,\n
word''')

# boolean 值判断
print(3 > 2)
print(False)
print(not True)

print(ord('A'))
print(chr(65))
print(ord('你'))

# bytes类型数据
print(b'ABC')
print('ABC'.encode('ascii'))

# print('你'.encode('ascii')) #异常代码，无法执行 UnicodeEncodeError
# 忽略错误字节
print('忽略错误写法==>', '你'.encode('ascii', errors='ignore'))
# 汉字正确写法
print('你'.encode('utf-8'))

# bytes处理成其他数据
# 英文字符两种方式都可以
print(b'ABC'.decode('ascii'))
print(b'ABC'.decode('utf-8'))
# 汉字只能在utf-8模式下
print(b'\xe4\xbd\xa0'.decode('utf-8'))
print('忽略错误写法==>', b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 统计字符
# 默认统计字符，对于bytes，统计的则是字节数、
# 一个中文字符经过utf-8编码后通常会占用3个字节
print(len('abc'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化数据
print('Hello,%s' % 'word')
print('hi,%s,%s' % ('Mr Li', 'Mr wang'))
# 增长率7%表示方法,需要通过%转译
print('增长率：%d%%' % 7)
print('增长率：%.2f%%' % 25.125)


# 1024*45= 46080
# I'm OK
# I am
#  Y
# \
# \
# 你是谁
#     握手哈岁哦
#     ha
# hello,\n
# word
# True
# False
# False
# 65
# A
# 20320
# b'ABC'
# b'ABC'
# 忽略错误写法==> b''
# b'\xe4\xbd\xa0'
# ABC
# ABC
# 你
# 忽略错误写法==> 中
# 3
# 6
# 6
# Hello,word
# hi,Mr Li,Mr wang
# 增长率：7 %
# 增长率：25.12%




