# Import the required libraries
import os
import mysql.connector

# Connect to bdd
def connect_bdd():
        mysql_host = os.getenv("MYSQL_HOST", "localhost")
        mysql_port = os.getenv("MYSQL_PORT", 3306)
        mysql_user = os.getenv("MYSQL_USER", "root")
        mysql_password = os.getenv("MYSQL_PASSWORD", "root")
        mysql_database = os.getenv("MYSQL_DATABASE", "birthday")

        mydb = mysql.connector.connect(
            host=mysql_host,
            port=mysql_port,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        
        return mydb