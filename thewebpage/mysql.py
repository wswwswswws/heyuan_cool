import pymysql

# 替换为你的数据库连接信息
host = "47.115.205.240"
user = "root"
password = "123456"
database = "huaming"

def insert(data) :
    print('Received Form Data:', data)
    # 提取数据
    name = data.get('name')
    gender = data.get('gender')
    phoneNumber = data.get('phoneNumber')
    position = data.get('position')
    salary = data.get('salary')

    try:
        # 建立数据库连接
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            # 执行插入语句
            # 执行插入语句
            sql = "INSERT INTO huamingce (`name`, `describe`, `reason`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, gender, position))

            # 执行查询语句
            select_query = 'SELECT * FROM huamingce'
            cursor.execute(select_query)

            # 获取查询结果
            result = cursor.fetchall()

        # 提交事务
        connection.commit()

        # 打印查询结果
        for row in result:
            print(row)

    except pymysql.Error as err:
        print(f"Error: {err}")

    finally:
        # 关闭连接
        if 'connection' in locals() and connection is not None:
            connection.close()
            print("MySQL连接已关闭")

