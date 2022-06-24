# MySQL in Linux Server: Create MySQL Output file (with Header)
SELECT 'column_1', 'column_2'
UNION ALL
SELECT *
FROM table_name
INTO OUTFILE 'output.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
;

# Linux Server: Move output.csv and Chown
sudo mv /var/lib/mysql/DB_NAME/output.csv /YOUR_PATH/ # (Default: /home/YOUR_NAME/output)
sudo chown YOUR_NAME:YOUR_NAME /home/buhm/output/output.csv

# Local: SCP
scp -P PORT_NUMBER YOUR_NAME@SERVER_IP:/YOUR_PATH/output.csv \YOUR_LOCAL_PATH\ # (Default: C:\Users\YOUR_NAME\Desktop)
scp -r -P PORT_NUMBER YOUR_NAME@SERVER_IP:/YOUR_PATH/output.csv \YOUR_LOCAL_PATH\ # (-r: All Files in DIR)
