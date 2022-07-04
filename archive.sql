# Modify Columns Type
ALTER TABLE table_name MODIFY col_name col_type;

# pymysql, InternalError: 1366, 'Incorrect String Value'
ALTER DATABASE [DB명] CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE [column명] CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Show Charset of Database
SHOW CREATE DATABASE DB_NAME;

# Change Charset of Database
ALTER DATABASE DB_NAME default character set = utf8mb4;
