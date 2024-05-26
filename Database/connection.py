# Install - mysql-connector-python

import mysql.connector

con = mysql.connector.connect(host='localhost',
                        user='root',
                        password='******',
                        database="mydb")
curs = con.cursor()
curs.execute("SELECT * FROM mydb.student")

for val in curs:
    print(val)

con.close()


# we need db setup for testing this code i dont have it in my setup
#
# try to install some db setup and you can check this code





