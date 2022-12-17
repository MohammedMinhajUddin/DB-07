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
    office_query = "SELECT officeCode, city FROM offices"
    office_cursor = cm_connection.cursor()
    office_cursor.execute(office_query)
    for row in office_cursor.fetchall():
        print("{}. {}".format(row[0], row[1]))
    office_cursor.close()

    office_code= input("Enter office number: ")
    employee_number = input ("Enter EmployeeID: ")
    first_name = input("Enter employee first name: ")
    last_name = input("Enter employee last name: ")
    email = last_name+first_name[0]+"@classicmodels.com"
    extension = input("Enter extension: ")
    job_title = input("Enter title: ")

    employee_query = ("INSERT INTO employees "
                   "(employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    employee_data = (employee_number, last_name,first_name, extension, email, office_code, job_title)
    try:
        employee_cursor = cm_connection.cursor()
        employee_cursor.execute(employee_query, employee_data)
        cm_connection.commit()
        print("Added employee")   
        employee_cursor.close()
    except mysql.connector.Error as err:
        print("\nEmployee not added")
        print("Error: {}".format(err))
    cm_connection.close()


