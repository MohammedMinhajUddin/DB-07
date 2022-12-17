import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user="cs509",
      password="cs509pw",
      host="127.0.0.1",
      database="mybusiness")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

# Display customers – form the query, execute the query, print results
else:  
    customer_cursor = cm_connection.cursor()
    customer_query = ("SELECT CustomerName, CustomerPhone FROM customerinfo")

    customer_cursor.execute(customer_query)

    for row in customer_cursor.fetchall():
        print("{} has Phone Number {}".format(row[0], row[1]))

    customer_cursor.close()
    cm_connection.close()
