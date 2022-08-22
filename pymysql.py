import pymysql
import pandas as pd

con = pymysql.connect(host='localhost', port=YOUR_MySQL_Port,
                      user='YOUR_MySQL_ID', password='YOUR_MySQL_PW',
                      db='DB_NAME', charset='utf8mb4',
                      autocommit=True, # 결과 DB 반영 (Insert or update)
                      cursorclass=pymysql.cursors.DictCursor # DB조회시 컬럼명을 동시에 보여줌
                     )
cur = con.cursor()

sql = "select * from table limit 30"
cur.execute(sql)
result = cur.fetchall()

df = pd.DataFrame(result)
df
