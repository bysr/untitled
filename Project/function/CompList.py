# 列表生成式

import os  # 导入os模块，模块的概念后面讲到


L = ['Java', 'C', 'Swift', 'Python', 123]

# 筛选出字符串以及字母小写显示
print([s.lower() for s in L if isinstance(s, str)])


print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录


# 生成式
g = (s.lower() for s in L if isinstance(s, str))
print(g)
print(next(g))  # java
print(next(g))  # c
print(next(g))  # swift
print('------------------------------')
for n in g:
    print(n)

