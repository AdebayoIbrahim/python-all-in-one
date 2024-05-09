# #this sis a module to add field text to the data base
# #first connect to the db
import mysql.connector

mydb = mysql.connector.connect(
user = "SetUp",
host = "localhost",
password = "setup123",
database = "forms"
)

mycursor = mydb.cursor()

def addDb(firstname,lastname):
    if firstname and lastname:
        # mycursor.close()
        #writting sql command to save to database
        sql = """INSERT INTO USERS(
        firstName,lastName
        )VALUES(%s,%s)"""
        mycursor.execute(sql,(firstname,lastname))
        #note_we-didnot-use format method here coz, it is prone to sql injection
        mydb.commit()
    else:
        return "Error Saving Into Data base"  
#close db
# mycursor.close()    


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

#now our function to accept user fields and save to the database
