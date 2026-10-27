import pymysql

# 把这里的 172.17.52.2 换成你刚才在 Kali 里查到的 IP！
try:
    conn = pymysql.connect(
        host='172.17.52.2',
        user='root',
        password='',
        charset='utf8mb4'
    )
    print("跨系统连接数据库成功！")

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS abyss;")
    cursor.execute("USE abyss;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            quantity INT DEFAULT 1
        );
    """)
    print("数据表创建成功！")

    cursor.close()
    conn.close()

except Exception as e:
    print("连接失败：", e)