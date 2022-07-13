'''
The Grand Beginning:
(sqlalchemy.exc.DataError: (pymysql.err.DataError) (1366, "Incorrect string value: ))

# 1
my.cnf -> not work

# 2
?charset -> not work

# 3
chunk_size = 1
try, except, else -> works
'''

from datetime import datetime
import encodings
from encodings.utf_8 import encode
from tarfile import ENCODING
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

mysql_id = 'YOUR_MYSQL_ID'
mysql_pw = 'YOUR_MYSQL_PW'
mysql_host = 'YOUR_HOST(Default: localhost)'
mysql_port = 'YOUR_PORT(Default: 3306)'
mysql_db_name = 'YOUR_MYSQL_DB_NAME'
mysql_table_name = 'YOUR_MYSQL_TABLE_NAME'
mysql_char_set = 'utf8mb4' # not used
mysql_encoding_set = 'utf8mb4' # not used
dir_path = 'YOUR_FILE_DIR_PATH'
dir_list = os.listdir(dir_path)
dir_len = len(dir_list)
chunk_size = 1
chunk_cnt = 1
engine = create_engine(f'mysql+pymysql://{mysql_id}:{mysql_pw}@{mysql_host}:{mysql_port}/{mysql_db_name}')
append_cnt = 1

df = pd.read_sas(dir_path + 'YOUR_SAS7DBAT_FILE_NAME.sas7bdat', chunksize = chunk_size)
df_list = []

for chunk in df:
    df_list.append(chunk)
    print("*** Table Data: ", chunk_cnt*chunk_size, " loaded ***")
    chunk_cnt += 1

print(len(df_list))
count_all_records = sum([len(x) for x in df_list])
print(count_all_records)

type(df_list[0])
print(df_list[0].columns)
print(len(df_list[0].columns))
print(df_list[0].head(5))

# It Works

err = []
err_cnt = 1

for x in df_list:
    try:
        x.to_sql(mysql_table_name, engine, index=False, if_exists='append')
    except:
        print("***************************")
        print("*** ", err_cnt, " error ***")
        print("***************************")
        err.append(err_cnt)
        err_cnt += 1
        pass
    else:
        print(append_cnt, "appended")
        append_cnt += 1

print(err)

print("***************************")
print("*           End           *")
print("***************************")
