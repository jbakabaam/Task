from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

engine = create_engine("mysql+pymysql://ID:PW@localhost:3306/DB_NAME")

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
    df_list[x].to_sql('TABLE_NAME', engine, index=False, if_exists='append')
    print(append_cnt, "chunk appended")
    append_cnt += 1
