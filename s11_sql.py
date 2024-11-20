# import pyodbc
#
# SERVER = '127.0.0.1'
# DATABASE = 'dotin'
# USERNAME = 'sa'
# PASSWORD = '123'
#
# connectionString = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
#
# conn = pyodbc.connect(connectionString)
#
# SQL_QUERY = "SELECT * FROM [dbo].[profile]"
# cursor = conn.cursor()
# cursor.execute(SQL_QUERY)
# for item in cursor.fetchall():
#     pass
#     # print(item)

# SQL_Query2 = "DELETE FROM [dbo].[profile] WHERE [Name] = 'Ali'"
# cursor.execute(SQL_Query2)
# cursor.commit()

# SQL_query3 = "UPDATE [dbo].[profile] SET [age] = 20 WHERE [Name] = 'Mona'"
# cursor.execute((SQL_query3))
# cursor.commit()

# name = 'Abbas'
# family = 'Bouazar'
# age = 26
# SQL_query4 = "INSERT INTO profile (name, family, age) VALUES (?,?,?);"
# cursor.execute(SQL_query4, name, family, age)
# cursor.commit()
#
# cursor.close()
# conn.close()


# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="D0tin@123"
#
# )
# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM dotin.organization")

# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
# from datetime import datetime
#
# created_time = datetime.now()
#
# query = "INSERT INTO `dotin`.`organization` (`employee_id`, `location`, `job_title`,`created_time`) VALUES (%s, %s, %s,%s)"
# values = (3320, "Qom", "Developer", created_time)
# mycursor.execute(query, values)
# mydb.commit()
#
# mycursor.close()
# mydb.close()


import mysql.connector
from datetime import datetime

hostx = "localhost"
userx = "root"
passwordx = "D0tin@123"

data = [(1000, "test", "test"), (1001, "test2", "test2")]


def db_connection(host, user, password):
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password)
    return mydb


def db_insert(item):
    connection = db_connection(hostx, userx, passwordx)
    mycursor = connection.cursor()
    query = "INSERT INTO `dotin`.`orsganization` (`employee_id`, `location`, `job_title`) VALUES (%s, %s, %s)"
    mycursor.execute(query, item)
    connection.commit()

    mycursor.close()
    connection.close()


for item in data:
    db_insert(item)
