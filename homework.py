import pymysql

pwd = input("请输入你的MySQL密码：")
conn = pymysql.connect(host='localhost',user='root',password=pwd,charset='utf8')
cursor = conn.cursor()

cursor.execute("create database if not exists music")
cursor.execute("use music")

cursor.execute("""create table if not exists singers (
    id int auto_increment primary key ,
    name varchar(255) ,
    gender char(2) ,
    age int ,
    phone char(11),
    debut_year int,
    representative_song varchar(255) 
)""")

cursor.execute("truncate table singers")

cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('周杰伦','男',45,'13800000001',2000,'七里香')")
cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('林俊杰','男',43,'13800000002',2003,'江南')")
cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('邓紫棋','女',32,'13800000003',2008,'光年之外')")
cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('刘若英','女',53,'13800000004',1995,'后来')")
cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('李荣浩','男',38,'13800000005',2010,'年少有为')")
conn.commit()

cursor.execute("select name,age from singers where age > 30")
print(cursor.fetchall())

cursor.execute("select name,representative_song from singers where gender ='女'")
print(cursor.fetchall())

cursor.execute("select name,debut_year from singers order by debut_year asc")
print(cursor.fetchall())

cursor.execute("update singers set age=46 where name='周杰伦'")
cursor.execute("update singers set representative_song='泡沫' where name='邓紫棋'")
conn.commit()

cursor.execute("select * from singers where phone ='13800000001'")
if cursor.fetchone():
    print("插入失败：手机号13800000001已存在")
else:
    cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('刘德华','男',55,'13800000001',1985,'忘情水') ")
    conn.commit()

cursor.execute("select * from singers where phone ='13800000006'")
if cursor.fetchone():
    print("插入失败：手机号13800000006已存在")
else:
    cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('陈奕迅','男',50,'13800000006',1996,'十年') ")
    conn.commit()

cursor.execute("delete from singers where name ='邓紫棋'")
conn.commit()

cursor.execute("select * from singers")
print(cursor.fetchall())

try:
    cursor.execute("select * from singers where phone ='13800000007'")
    if not cursor.fetchone():
        cursor.execute("insert into singers(name,gender,age,phone,debut_year,representative_song) values('王菲','女',55,'13800000007',1996,'红豆')")
    raise Exception("模拟出错")
except Exception as e:
    conn.rollback()
    print("事务已回滚")

cursor.execute("select * from singers")
print(cursor.fetchall())

cursor.close()
conn.close()