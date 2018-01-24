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

sql="select * from user"
cursor.execute(sql)

print(cursor.rowcount)


rs = cursor.fetchall()
for row in rs:
    print("userid=%s,username=%s"%row)

cursor.close()
conn.close()
