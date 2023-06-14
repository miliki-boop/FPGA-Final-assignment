from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
CORS(app)
DATABASE = os.path.join(BASE_DIR, "mydatabase.db")  # 替换为你的SQLite数据库文件路径

def query_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # 执行数据库查询操作，根据需求编写查询语句
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/query', methods=['POST'])
def handle_post_request():
    # 解析POST请求中的数据
    data = request.get_json()
    
    # 执行查询操作，获取数据
    result = query_database()
    print(result)
    # 构建响应数据
    response = {
        'messages': result
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=55090)  # 替换为你希望的端口号
