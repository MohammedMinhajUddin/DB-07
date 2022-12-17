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
    employee_cursor = cm_connection.cursor()
    employee_query = ("SELECT employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle FROM employees")

    employee_cursor.execute(employee_query)

    for row in employee_cursor.fetchall():
        print("EmployeeNumber= {}, LastName= {}, FirstName= {}, Extension = {}, Email= {}, OfficeCode = {}, JobTitle = {} ".format(row[0], row[1],row[2],row[3],row[4],row[5],row[6]))

    employee_cursor.close()
    cm_connection.close()
