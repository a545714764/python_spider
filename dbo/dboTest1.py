import pymysql

conn = pymysql.Connect(
    host = '127.0.0.1',
    port=3306,
    user='root',
    passwd='734368048',
    db='imooc',
    charset='utf8'
)
cursor=conn.cursor()

print(conn)
print(cursor)

conn.close()
cursor.close()