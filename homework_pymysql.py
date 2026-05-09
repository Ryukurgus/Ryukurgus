import pymysql

pwd = input("请输入你的密码：")
conn = pymysql.connect(
    host='localhost',
    user='root',
    password=pwd,
    database='music',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()

cursor.execute("select * from singers where phone='13800000099'")
if not cursor.fetchone():
    cursor.execute(
        "insert into singers(name,gender,age,phone,debut_year,representative_song) values(%s,%s,%s,%s,%s,%s)",
        ("测试歌手", "保密", 20, "13800000099", 2020, "测试歌曲")
    )
    conn.commit()

malicious_input = "测试歌手' OR '1'='1"

print("错误方式（拼接字符串）结果：")
bad_sql = f"select * from singers where name='{malicious_input}'"
cursor.execute(bad_sql)
for row in cursor.fetchall():
    print(row)
print("\n正确方式（参数化查询）结果：")
good_sql = "select * from singers where name=%s"
cursor.execute(good_sql, (malicious_input,))
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()