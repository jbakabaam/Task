###############
#  SAS To DF  #
###############

import pandas as pd
df = pd.read_sas("filename.sas7bdat", chunksize = 1000000)
dfs = []

cnt = 1
for chunk in df:
    dfs.append(chunk)
    print("*** ", cnt, "회 진행 중 ***")
    cnt += 1

df_final = pd.concat(dfs)

print(len(dfs))
count_all_records = sum([len(x) for x in dfs])
print(count_all_records)

type(dfs[0])

print(dfs[0].columns)
print(dfs[0].head(5))

dataframe = pd.DataFrame(df_final)
dataframe.to_csv("outputfilename.csv", header=False, index=False)


###############
# DF To MYSQL #
#  localhost  #
###############

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

engine = create_engine("mysql+pymysql://localmysql_id:localmysql_pw@localhost:3306/dbname") # MYSQL_ID:MYSQL_PW@localhost:3306/DBNAME

df_final.to_sql('test220524', engine, index=False) # DataFrame -> MySQL // test220524 : 만들 테이블 이름
