# sas7bdat to mysql database (pandas data frame)

from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

mysql_id = 'YOUR_MYSQL_ID'
mysql_pw = 'YOUR_MYSQL_PW'
mysql_host = 'YOUR_MYSQL_HOST (DEFAULT: localhost)'
mysql_port = 'YOUR_MYSQL_PORT (DEFAULT: 3306)'
mysql_db_name = 'YOUR_MYSQL_DB_NAME'
mysql_table_name = 'YOUR_MYSQL_TABLE_NAME'
dir_path = '/YOUR_DIR_PATH/'
dir_list = os.listdir(dir_path)
dir_len = len(dir_list)

engine = create_engine(f'mysql+pymysql://{mysql_id}:{mysql_pw}@{mysql_host}:{mysql_port}/{mysql_db_name}')

df = pd.read_sas("FILENAME.sas7bdat", chunksize = 1000000)
df_list = []
chunk_cnt = 1
chunk_size = 1000000

for chunk in df:
    df_list.append(chunk)
    print("*** Table Data: ", chunk_cnt*chunk_size, " Loaded ***")
    chunk_cnt += 1

print(len(df_list))
count_all_records = sum([len(x) for x in df_list])
print(count_all_records)

type(df_list[0])
print(df_list[0].columns)
print(len(df_list[0].columns))
print(df_list[0].head(5))

append_cnt = 1
for x in range(len(df_list)):
    df_list[x].to_sql(mysql_table_name, engine, index=False, if_exists='append')
    print(append_cnt, "chunk appended")
    append_cnt += 1
