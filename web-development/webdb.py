# #this sis a module to add field text to the data base
# #first connect to the db
# import mysql.connector

# mydb = mysql.connector.connect(
# username = "SetUp",
# host = "localhost",
# password = "setup123",
# database = "forms"
# )

# mycursor = mydb.cursor()

# sql  = """CREATE TABLE Users(
# firstName VARCHAR(225),
# lastName VARCHAR(225),
# user_id INT AUTO_INCREMENT PRIMARY KEY
# )"""

# mycursor.execute(sql)


# sql = "DESCRIBE USERS"
# mycursor.execute(sql)

# for j in mycursor:
#     print(j)

#the above is for creating database and tables in it