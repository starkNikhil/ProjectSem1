from database.myconnection import connect_to_mysql

show_employee = "SELECT * FROM employees WHERE Emp_Id = %s"
query = "SELECT * FROM employees WHERE {column} = %s"
update_student = "UPDATE employees set {} where Emp_Id = {}"



# this is a dictionary use to change the name temporarily.................................
employee_column_name = {"Professor_ID" : "Emp_Id" ,  "Professor_Name" : "Name"}
# ..........................................................................................


def db_data_to_dict(row):
    
    Emp_Id, Name, Contact_Number, Email_Id = row
    
    employee = {
        "Emp_Id": Emp_Id,
        "Name": Name,
        "Contact_Number": Contact_Number,
        "Email_Id": Email_Id,
        
    }
    return employee


def dict_to_db_data(employee):
    return (
        employee["Emp_Id"],
        employee["Name"],
        employee["Contact_Number"],
        employee["Email_Id"],
        
    )


# .......................................search function..............................................
# .....................................................................................................


def get_by_employee(column, value):
    valid_columns = ["Emp_Id", "Name", "Contact_Number", "Email_Id"]
    
    if column not in valid_columns:
        print(f"Error: Invalid column name '{column}'.")
        return []

    query = f"SELECT * FROM employees WHERE {column} = %s"
    # print(query)
    cnx = connect_to_mysql()
    if cnx and cnx.is_connected():
        cursor = cnx.cursor()
        print(query)
        print(value)
        cursor.execute(query, (value,))
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        
        if len(rows) >= 1:
            return [db_data_to_dict(row) for row in rows]  # Return all matching rows as a list of dictionaries
        else:
            print("No records found matching the provided details.")
            return []
    else:
        print("Error: Unable to connect with MySQL")
        return []
    
# ................................update function......................................................
# ......................................................................................................

def make_set_clause(employee):
  set_clause = []
  for key, val in employee.items():
    base_str = "{}={}" if key == "active" else "{}='{}'"
    set_clause.append(base_str.format(employee_column_name.get(key, key), val))
  return ",".join(set_clause)


def update_emp(employee, Emp_Id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    
    query_template = f"UPDATE employees SET {make_set_clause(employee)} WHERE Emp_Id = %s"
    
    # Prepare the values tuple for placeholders in the query
    values = (Emp_Id,)
    print(query_template)
    print(values)
    cursor.execute(query_template,values)
    cnx.commit()
    cursor.close()
    cnx.close()
    return get_by_id_employee(Emp_Id)
  else:
    print("Error : Unable to connect with Mysql")
    return {}
  



# ......................................search by primary key(Emp_Id)...........................
# .....................................................................................................


def get_by_id_employee(id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    cursor.execute(show_employee, (id,))
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    cnx.close()
    if(len(rows) >= 1): 
      return db_data_to_dict(rows[0])
    else:
      return {}
  else:
    print("Error : Unable to connect with Mysql")
    return {}
  