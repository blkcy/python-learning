import pymysql

try:
    # 1. 建立连接，这次直接连到 abyss 数据库
    conn = pymysql.connect(
        host='172.17.52.2',
        user='root',
        password='blkcy0123',
        database='abyss',  # 直接指定使用这个库
        charset='utf8mb4'
    )

    cursor = conn.cursor()
    print("连接成功，开始操作数据！\n")

    # 2. 增（Insert）：往表里塞两件战利品
    # 注意：这里用 %s 占位符，后面传元组，可以防止 SQL 注入（黑客常用手段）
    cursor.execute("INSERT INTO items (name, quantity) VALUES (%s, %s);", ("齿轮", 5))
    cursor.execute("INSERT INTO items (name, quantity) VALUES (%s, %s);", ("蜜蜡", 2))

    # 【关键】必须提交事务，数据才会真正写入硬盘
    conn.commit()
    print("成功添加了 齿轮 和 蜜蜡！\n")

    # 3. 查（Select）：把表里的数据读出来
    cursor.execute("SELECT id, name, quantity FROM items;")
    results = cursor.fetchall()  # 获取所有结果

    print("--- 当前库存 ---")
    for row in results:
        # row 是一个元组，比如 (1, '齿轮', 5)
        print(f"ID: {row[0]}, 物品: {row[1]}, 数量: {row[2]}")

    cursor.close()
    conn.close()

except Exception as e:
    print("出错了：", e)