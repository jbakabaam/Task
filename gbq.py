# prep
'''
GCP > Make a Project
    > Make a Storage
    > Make a Bucket
    > Make a Service Account
    > Make an Authentication Key (json)
    > User Authorization = Owner
'''

# import libs
import glob
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage
import gspread
import os
import pandas_gbq
import pandas as pd
import numpy as np

# gbq settings
key = 'YOUR_GCP_KEY_JSON'
project_id = 'YOUR_GBQ_PROJECT_ID'
key_path = glob.glob(key)[0]
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials = credentials, project = project_id)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= key

# print buckets
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
print(buckets)

# upload to gcp
bucket_name = 'YOUR_BUCKET_NAME'
source_file_name = 'YOUR_PATH/FILENAME.FILETYPE'
destination_blob_name = 'YOUR_FILENAME_AT_GCP.FILETYPE'
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)

# download from gcp
bucket_name = 'YOUR_BUCKET_NAME'
source_blob_name = 'YOUR_FILENAME_AT_GCP.FILETYPE'
destination_file_name = 'YOUR_FILENAME.FILETYPE'
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)

# gbq_query
sql = '''
YOUR_QUERY
'''
query_job = client.query(sql)
df = query_job.to_dataframe()
df

# dataframe to gbq_table
target_table = 'YOUR_DATASET.YOUR_TABLE'
job_location = 'YOUR_DATASET_LOCATION' # ex: us
df.to_gbq(target_table, project_id=project_id, if_exists='replace',
          location=job_location, progress_bar=True, credentials=credentials)

# create a gbq_table
sql = """
CREATE TABLE `YOUR_DATASET.YOUR_TABLE_NAME`
(
    col_1 string,
    col_2 int64,
    col_3 date
)
"""
query_job = client.query(sql)

# drop a gbq_table
sql = """
DROP TABLE `YOUR_DATASET.YOUR_TABLE`
"""
query_job = client.query(sql)

# read gspread to dataframe
gc = gspread.service_account(filename=key)
spreadsheet_url = 'YOUR_GOOGLE_SPREADSHEET_URL'
doc = gc.open_by_url(spreadsheet_url) # open gspread
worksheet = doc.worksheet('시트1') # sheet choice
df = pd.DataFrame(worksheet.get_all_records())
df

# read multiple files to gbq tables
dir_path = '/YOUR_DIR_PATH/'
dir_list = os.listdir(dir_path)
dir_len = len(dir_list)
df_len_list = []

print('=====================================================')
print('=====================================================')
print('=====================================================')

for file_name in dir_list:
    print('Start Time: ', datetime.now())
    print('***** ', dir_len, ' file(s) left *****')
    print('*** Now: ', file_name, ' ***')
    df = pd.read_csv(dir_path + file_name, sep=',')
    df_list = []
    df_len_list.append(len(list(df.columns)))
    
    # Dataframe to GBQ Table
    target_dataset = 'buhm.'
    target_tbl = os.path.splitext(file_name)[0]
    target_table = target_dataset+target_tbl
    job_location = 'us'

    df.to_gbq(target_table, project_id=project_id, if_exists='replace',
          location=job_location, progress_bar=True, credentials=credentials)
          
    print('End Time: ', datetime.now())
    print('-----------------------------------------------------')
    dir_len-=1

print('=====================================================')
print('=====================================================')
print('=====================================================')
