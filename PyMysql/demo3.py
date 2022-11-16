import pymysql.cursors

db = pymysql.connect(
        host='localhost',
        user='root',
        password = "admin",
        db='demo1',
        cursorclass=pymysql.cursors.DictCursor)

with db.cursor() as cur:
    sql = "select * from student"
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
