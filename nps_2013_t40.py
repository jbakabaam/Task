from datetime import datetime
import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb

engine = create_engine("mysql+pymysql://ID:PW@localhost:3306/DB_NAME")
dir_list = os.listdir('/PATH/')
dir_len = len(dir_list)

for path_detail in dir_list:
    print("*** ", dir_len, " file(s) left ***")
    print("*** Now: ", path_detail, " ***")
    df = pd.read_csv('/PATH/' + path_detail, chunksize = 1000000,
    names=['SPEC_ID_SNO', 'SICK_SNO', 'SICK_DGSBJT_CD', 'SICK_CD', 'DMD_DGSBJT_CD'], index_col=False)
    df_list = []
    chunk_cnt = 1
    chunk_size = 1000000

    for chunk in df:
        df_list.append(chunk)
        print("*** Table Data: ", chunk_cnt*chunk_size, " Loaded ***")
        chunk_cnt += 1

    print(len(df_list))
    count_all_records = sum([len(x) for x in df_list])
    print("*** Total: ", count_all_records, " ***")

    type(df_list[0])
    print(df_list[0].columns)
    print(len(df_list[0].columns))
    
    append_cnt = 1
    for x in range(len(df_list)):
        df_list[x].to_sql('t40', engine, index=False, if_exists='append')
        print(append_cnt, "chunk appended")
        append_cnt += 1
    
    dir_len -= 1
