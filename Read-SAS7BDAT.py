#########################
# Read SAS To Pandas DF #
#########################

from datetime import datetime
import pandas as pd
df = pd.read_sas("filename.sas7bdat", chunksize = 1000000) # Chunk = 1M
dfs = []

cnt = 1
chunksz = 1000000
print("********** Start: ", datetime.now(), " **********")
for chunk in df:
    dfs.append(chunk)
    print("*** Table Data: ", cnt*chunksz, " Loaded ***")
    cnt += 1
print("********** The End of Process ********** ")
print("********** Close: ", datetime.now(), " **********")

print(len(dfs)) # Chunk 개수 = n개
count_all_records = sum([len(x) for x in dfs])
print(count_all_records) # x 개 (1M * n세트)

type(dfs[0])
print(dfs[0].columns)
print(len(dfs[0].columns))
print(dfs[0].head(5))

################################
# DF To MYSQL by Chunk Process #
################################

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

engine = create_engine("mysql+pymysql://id:pw@localhost:3306/DBNAME") # MYSQL_ID:MYSQL_PW@localhost:3306/DBNAME

for_cnt = 1
for_num = len(dfs) + 1
print(for_num)
for x in range(for_num):
    dfs[x].to_sql('table_name', engine, index=False, if_exists='append')
    print(for_cnt, "chunk appended")
    for_cnt += 1

###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
###################################################################################################################################

##################################
# If You Need, Follow the below  # 
# DF To SQL by Concat(Full Size) #
##################################

df_final = pd.concat(dfs)

type(df_final)
print(df_final.columns)
print(len(df_final.columns))
print(df_final.head(5))

print("********** To CSV: ", datetime.now(), " **********")
df_final.to_csv("save.csv", header=True, index=True)
print("********** The End of Process: ", datetime.now(), " **********")

############################   
# DF To MYSQL by Full Size #
############################

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

engine = create_engine("mysql+pymysql://id:pw@localhost:3306/DBNAME") # MYSQL_ID:MYSQL_PW@localhost:3306/DBNAME

df_final.to_sql('table_name', engine, index=True, if_exists='append', chunksize=100000) # DataFrame -> MySQL // table_name : 만들 테이블 이름
