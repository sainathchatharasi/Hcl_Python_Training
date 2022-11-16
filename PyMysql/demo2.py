import pymysql
db = pymysql.connect(
        host='localhost',
        user='root',
        password = "admin",
        db='demo1',
        cursorclass=pymysql.cursors.DictCursor)

cur = db.cursor()
query = 'INSERT INTO student VALUES("jhon","walker",22,"89930vdf67")'
query1 = 'SELECT * from student'
try:
    cur.execute(query)
    db.commit() #commint writing to the database
    cur.execute(query1)
    print(cur.fetchone())
    db.commit()
except:
    db.rollback()
db.close()
