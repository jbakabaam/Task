# NPS_2013_t53.txt files

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

for path_detail in dir_list:
    print(path_detail)
    df = pd.read_csv('/PATH/' + path_detail, chunksize = 1000000,
    names=['SPEC_ID_SNO','LN_NO','PRSCP_GRANT_NO','FQ1_MDCT_QTY','DY1_MDCT_QTY','TOT_INJC_DDCNT_EXEC_FQ','TOT_USE_QTY_OR_EXEC_FQ','UNPRC','AMT','GNL_NM_CD'],
                     index_col=False)
    df_list = []
    cnt = 1
    chunksz = 1000000

    for chunk in df:
        df_list.append(chunk)
        print("*** Table Data: ", cnt*chunksz, " Loaded ***")
        cnt += 1

    print(len(df_list))
    count_all_records = sum([len(x) for x in df_list])
    print(count_all_records)

    type(df_list[0])
    print(df_list[0].columns)
    print(len(df_list[0].columns))

    for_cnt = 1
    for x in range(len(df_list)):
        df_list[x].to_sql('t53', engine, index=False, if_exists='append')
        print(for_cnt, "chunk appended")
        for_cnt += 1
