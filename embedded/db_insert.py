import sqlite3

def insert_user_data(text, part):
    # 创建数据库连接
    conn = sqlite3.connect('mydatabase.db')

    # 创建游标对象
    cursor = conn.cursor()

    # 插入数据
    cursor.execute("INSERT INTO users (text, part) VALUES (?, ?)", (text, part))

    # 提交更改
    conn.commit()

    # 关闭连接
    conn.close()
