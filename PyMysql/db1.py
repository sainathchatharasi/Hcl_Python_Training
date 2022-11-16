import pymysql.cursors

db = pymysql.connect(
        host='localhost',
        user='root',
        password = "admin",
        db='demo1',
        cursorclass=pymysql.cursors.DictCursor)

sql = "delete from student where age>12"
cur = db.cursor()
try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
