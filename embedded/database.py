import sqlite3

# 创建数据库连接
conn = sqlite3.connect('mydatabase.db')

# 创建游标对象
cursor = conn.cursor()

# 创建表格
cursor.execute('''CREATE TABLE users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   text TEXT,
                   part TEXT)''')


# 提交更改
conn.commit()


# 关闭连接
conn.close()
