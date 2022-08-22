import pymysql
import pandas as pd

mysql_host = 'localhost'
mysql_port = YOUR_MySQL_Port # Only Use INT
mysql_id = 'YOUR_MySQL_ID'
mysql_pw = 'YOUR_MySQL_PW'
mysql_db_name = 'YOUR_DB_NAME'
mysql_char_set = 'utf8mb4'
mysql_auto_commit = True

con = pymysql.connect(host=mysql_host, port=mysql_port,
                      user=mysql_id, password=mysql_pw,
                      db=mysql_db_name, charset=mysql_char_set,
                      autocommit=mysql_auto_commit,
                      cursorclass=pymysql.cursors.DictCursor
                     )
cur = con.cursor()

sql = "select * from table limit 10"
cur.execute(sql)
result = cur.fetchall()

df = pd.DataFrame(result)
df
