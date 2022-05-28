import pymysql
# 資料庫設定
db_settings = {
    "host": "qsnake.ddns.net",
    "port": 3306,
    "user": "manager",
    "password": "20011214",
    "db": "nccu_drinks",
    "charset": "utf8"
}
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        command = "SELECT * FROM Store "
        command1 = 'INSERT INTO Store(Store_ID,Store_Name,E_ID) VALUES ("1122","5","36426052");'
        cursor.execute(command)
        cursor.execute(command1)  # (Store_ID,Store_Name,E_ID,Store_Pic)
        print(command1)
        result = cursor.fetchall()
        print(result)

        # cursor.execute(command1)
    # 取得所有資料

        # print(command1)
        # result = cursor.fetchall()
        # print(result)

# 新增資料SQL語法

        # 資料表相關操作
except Exception as ex:
    print(ex)
