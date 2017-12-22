# 二进制流操作
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(f.getvalue().decode('utf-8'))

# 读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
