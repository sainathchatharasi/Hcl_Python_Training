import pymysql
db = pymysql.connect(
        host='localhost',
        user='root',
        password = "admin",
        db='demo1',
        cursorclass=pymysql.cursors.DictCursor)

cur = db.cursor()
    # Select query
cur.execute("SELECT VERSION();")
output = cur.fetchone()

print(output)
