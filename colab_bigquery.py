import glob
from google.cloud import bigquery
from google.oauth2 import service_account
from google.colab import drive
drive.mount('/content/drive')

key = 'YOUR_JSON_KEY' # '/Google_Drive_Path/abcd-1234-XYZ77BLAH.json'
project_id = 'YOUR_PROJECT_ID' # 'abcd-1234'
key_path = glob.glob(key)[0]
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials = credentials, project = project_id)

sql = """
select *
from table
limit 5
"""
query_job = client.query(sql)
df = query_job.to_dataframe()
df.head()
