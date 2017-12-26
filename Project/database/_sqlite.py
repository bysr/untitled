# 导入sqlite驱动
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
con = sqlite3.connect('test.db')
# 创建一个Cursor
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
# 插入一条数据
cursor.execute('INSERT INTO user (id, name) VALUES (\'3\', \'Michael\')')
# 获取插入的行数
count = cursor.rowcount
print(count)
# 关闭cursor
cursor.close()
# 提交事务
con.commit()
# 关闭
con.close()

# 查询结果
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM user WHERE id=?', ('2',))
values = cursor.fetchall()
print(values)
cursor.close()
con.close()
