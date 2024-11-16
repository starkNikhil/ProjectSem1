from database.myconnection import connect_to_mysql


show_marks = "SELECT * FROM subject_marks WHERE SR_No = %s"
query = "SELECT * FROM subject_marks WHERE {column} = %s"
update_student = "UPDATE subject_marks set {} where SR_No = {}"



# this is a dictionary use to change the name temporarily.................................
marks_column_name = {"Subject_Marks" : "Marks"}
# ..........................................................................................



def db_data_to_dict(row):
    
    SR_No, Std_Id, Sub_Id, Marks, Grade, Semester = row
    
    marks = {
        "SR_No": SR_No,
        "Std_Id": Std_Id,
        "Sub_Id": Sub_Id,
        "Marks": Marks,
        "Grade": Grade,
        "Semester": Semester
        
    }
    return marks


def dict_to_db_data(marks):
    return (
        marks["SR_No"],
        marks["Std_Id"],
        marks["Sub_Id"],
        marks["Marks"],
        marks["Grade"],
        marks["Semester"]
        
    )

# ............................search function...................................................
# ..............................................................................................


def get_by_marks(column, value):
    valid_columns = ["SR_No", "Std_Id", "Sub_Id", "Marks", "Grade", "Semester"]
    
    if column not in valid_columns:
        print(f"Error: Invalid column name '{column}'.")
        return []

    query = f"SELECT * FROM subject_marks WHERE {column} = %s"
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
    

# ..............................update function.............................................
# ...........................................................................................
def make_set_clause(marks):
  set_clause = []
  for key, val in marks.items():
    base_str = "{}={}" if key == "active" else "{}='{}'"
    set_clause.append(base_str.format(marks_column_name.get(key, key), val))
  return ",".join(set_clause)


def update_marks(marks, SR_No):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    
    query_template = f"UPDATE subject_marks SET {make_set_clause(marks)} WHERE SR_No = %s"
    
    # Prepare the values tuple for placeholders in the query
    values = (SR_No,)
    print(query_template)
    print(values)
    cursor.execute(query_template,values)
    cnx.commit()
    cursor.close()
    cnx.close()
    return get_by_id_marks(SR_No)
  else:
    print("Error : Unable to connect with Mysql")
    return {}
  
# ...............search by primary key(SR_No).....................................................
# ................................................................................................

def get_by_id_marks(id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    cursor.execute(show_marks, (id,))
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