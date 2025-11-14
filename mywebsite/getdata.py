# # import mysql.connector

# # 1 connect to database
# def connectDB():
#     ''' Connect to SQL Database'''
#     return mysql.connector.connect(
#         host='localhost', 
#         user='root',
#         password='sqluser',
#         database='sakila'     # connect to this database
#     )
# # 2 fetch data from SQL
# def fetchData():
#     mydb = connectDB()
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT customer_id, first_name, last_name, email FROM customer ORDER BY last_name LIMIT 20 ")
#     myresult = mycursor.fetchall()
#     for x in myresult:
#         print(x)

# # 3 format data as HTML table
# def formatTable():
#     for x in myresult:
#         print(x)

# # 4 write HTML table to a html file
# def writeHTML():
#     pass
# #--------------------------------------------------------


# fetchData()
# formatTable()
# writeHTML()