from database.myconnection import connect_to_mysql


show_student = "SELECT * FROM student WHERE Std_Id = %s" 

query = "SELECT * FROM student WHERE {column} = %s"

update_student = "UPDATE student set {} where Std_Id = {}"


# this is a dictionary use to change the name temporarily...........
student_column_name = {"Date_Of_Birth" : "Date_Of_Birth", "Fathers_name" : "Guardian_Name", "Contact_Number" : "Contact_Number"}
# ..............................................................................


def db_data_to_dict(row):
    
    Std_Id, Name, Email_Id, Date_Of_Birth,Guardian_Name, Nationality, Gender, Contact_Number, Address = row
    
    student = {
        "Std_Id": Std_Id,
        "Name": Name,
        "Email_Id": Email_Id,
        "Date_Of_Birth": Date_Of_Birth,
        "Guardian_Name": Guardian_Name,
        "Nationality": Nationality,
        "Gender": Gender,
        "Contact_Number": Contact_Number,
        "Address": Address
    }
    return student


def dict_to_db_data(student):
    return (
        student["Std_Id"],
        student["Name"],
        student["Email_Id"],
        student["Date_Of_Birth"],
        student["Guardian_Name"],
        student["Nationality"],
        student["Gender"],
        student["Contact_Number"],
        student["Address"]
    )


# ..................................search function..................................................
# ...................................................................................................

def get_by_column(column, value):
    valid_columns = ["Std_Id", "Name", "Email_Id", "Date_Of_Birth","Guardian_Name", "Nationality", "Gender", "Contact_Number", "Address"]
    
    if column not in valid_columns:
        print(f"Error: Invalid column name '{column}'.")
        return []

    query = f"SELECT * FROM student WHERE {column} = %s"
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
    


#........................................ update function............................................
# ...................................................................................................


def make_set_clause(student):
  set_clause = []
  for key, val in student.items():
    base_str = "{}={}" if key == "active" else "{}='{}'"
    set_clause.append(base_str.format(student_column_name.get(key, key), val))
  return ",".join(set_clause)


def update_std(student, Std_Id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    
    query_template = f"UPDATE student SET {make_set_clause(student)} WHERE Std_Id = %s"
    
    # Prepare the values tuple for placeholders in the query
    values =  (Std_Id,)
    print(query_template)
    print(values)
    cursor.execute(query_template,values)
    cnx.commit()
    cursor.close()
    cnx.close()
    return get_by_id(Std_Id)
  else:
    print("Error : Unable to connect with Mysql")
    return {}
    
# ...................................search by primary key(Std_Id)....................................
# .....................................................................................................


def get_by_id(id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    cursor.execute(show_student, (id,))
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
  

  

