import psycopg2
from psycopg2.extras import RealDictCursor
import time
import os

database = os.environ.get('POSTGRES_DB')
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('host')

def connect():
    while True:
        try:
            # Connect to an existing database
            print("CONNECTING TO DATABASE")
            conn = psycopg2.connect(host=host, database=database, user=user, password=password,cursor_factory=RealDictCursor)

            cursor = conn.cursor()
            print("DATABASE CONNECTION WAS SUCCESSFUL!!!")

            cursor.execute("""CREATE TABLE IF NOT EXISTS regtable(
                id serial,
                firstname varchar(30) NOT NULL,
                middlename varchar(30),
                lastname varchar(30) NOT NULL,
                gender varchar(6),
                address_str varchar(30) NOT NULL,
                address_nr varchar(6) NOT NULL,
                postbox varchar(10) NOT NULL,
                city varchar(15) NOT NULL,
                email varchar(30) PRIMARY KEY,
                password varchar(30) NOT NULL,
                account_created_at timestamp with time zone,
                last_login timestamp with time zone
                
                )""")
            conn.commit()

            print("regtable TABLE CREATED SUCCESSFULLY!!!")
            return conn
            break

        except Exception as error:
            print("CONECTION TO DATABSE FAILED")
            print("Error: ", error)
            print("RECCONNECTING IN 4 SECS")
            time.sleep(4)
