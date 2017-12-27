# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 导入我们自己编写的application函数:
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
from Project.web.hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
