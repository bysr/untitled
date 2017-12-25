# 正则表达式学习
import re

s = r'ABC\-001'
a = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# 返回match对象
print(a)
if a:
    print('ok')
else:
    print('failed')

b = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# 不匹配返回None
print(b)

test = '用户输入的字符串'
if re.match(r'用户输入的字符串', test):
    print('ok')
else:
    print('failed')

# 切分字符串
a = 'a b  c'.split(' ')
print(a)
# ['a', 'b', '', 'c'] 无法识别连续空格
# 　用正则表达式来把不规范的输入转化成正确的数组
b = re.split(r'[\s\,]+', 'a b  c')
c = re.split(r'[\s\,]+', 'a,b, c  d')
print(b)
print(c)

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
# print(m.group(3)) 不存在

# 贪婪匹配
# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
a = re.match(r'^(\d+)(0*)$', '102300').groups()
print(a)

# ('102300', '')
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
b = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(b)
