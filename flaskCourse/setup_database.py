import mysql.connector
import os
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv()
print("connecting...")
try:
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuário ou senha")
    else:
        print(err)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`;")

# CREATING TABLES

TABLES = {}
TABLES["champions"] = (
    """
        CREATE TABLE `champions`(
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `champion_name` VARCHAR(30) NOT NULL,
        `lane` VARCHAR(10) NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
        """
)
TABLES["users"] = (
    """
        CREATE TABLE `users`(
        `first_name` VARCHAR(30) NOT NULL,
        `last_name` VARCHAR(30) NOT NULL,
        `username` VARCHAR(30) NOT NULL,
        `password` VARCHAR(100) NOT NULL,
        PRIMARY KEY (`username`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
        """
)

for table_name in TABLES:
    sql_table = TABLES[table_name]
    try:
        print(f"criando tabela {table_name}:", end=" ")
        cursor.execute(sql_table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("this table already exists")
        else:
            print(err.msg)
    else:
        print("OK")

# Adding users
users_sql = (
    "INSERT INTO users(username,first_name,last_name,password) VALUES (%s,%s,%s,%s)"
)
users = [("rik", "Henrique", "Rodrigues", "123"), ("ana", "Ana", "Rodrigues", "456")]
cursor.executemany(users_sql, users)
cursor.execute("SELECT * FROM jogoteca.users;")
print(" ------------- USERS -------------------")
for user in cursor.fetchall():
    print(user[1])

# Adding champions

champions_sql = "INSERT INTO champions(champion_name,lane) VALUES (%s,%s)"
champions = [
    ("Lulu", "support"),
    ("Jhin", "bottom"),
    ("Zed", "mid"),
    ("Nunu & Willump", "jungle"),
    ("Akali", "top"),
]
cursor.executemany(champions_sql, champions)
print(" ------------- CHAMPIONS -------------------")
cursor.execute("SELECT * FROM jogoteca.champions;")

for champion in cursor.fetchall():
    print(champion[1])

# Commit changes
conn.commit()
cursor.close()
conn.close()
