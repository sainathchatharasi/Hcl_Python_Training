import pymysql.cursors

db = pymysql.connect(
        host='localhost',
        user='root',
        password = "admin",
        db='demo1',
        cursorclass=pymysql.cursors.DictCursor)

sql = "create table employee (fname varchar(100),lname varchar(100),age int,sapid varchar(20));"
cur = db.cursor()
try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
