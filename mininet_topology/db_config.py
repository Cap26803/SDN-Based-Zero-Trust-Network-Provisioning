import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="ztn_user",
        password="Ztn@1234!",
        database="sdn_ztn",
        port=3306
    )

