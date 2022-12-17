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

else:
    employee_last = input("Enter employee last name of employee to delete ")


    employee_query = ("DELETE FROM employees "
                      "WHERE lastName = %s")
    employee_data = (employee_last,)
    try:
        employee_cursor = cm_connection.cursor()
        employee_cursor.execute(employee_query, employee_data)
        cm_connection.commit()
        print("Deleted employee")
        employee_cursor.close()
    except mysql.connector.Error as err:
        print("\nEmployee not updated")
        print("Error: {}".format(err))
    cm_connection.close()
