from database.myconnection import connect_to_mysql

show_subject = "SELECT * FROM subjects WHERE Sub_Id = %s" 
query = "SELECT * FROM subjects WHERE {column} = %s"
update_subject = "UPDATE subjects set {} where Sub_Id = {}"


# this is a dictionary use to change the name temporarily...........
subject_column_name = {"Subject_Code" : "Sub_Id", "Subject" : "Sub_Name"}
# ..............................................................................


def db_data_to_dict(row):
    
    Sub_Id, Sub_Name, Faculty_Name, Emp_Id = row
    
    subject = {
        "Sub_Id": Sub_Id,
        "Sub_Name": Sub_Name,
        "Faculty_Name": Faculty_Name,
        "Emp_Id": Emp_Id
        
    }
    return subject


def dict_to_db_data(subject):
    return (
        subject["Sub_Id"],
        subject["Sub_Name"],
        subject["Faculty_Name"],
        subject["Emp_Id"]
        
    )


# .....................................search function................................................
# ....................................................................................................

def get_by_subjects(column, value):
    valid_columns = ["Sub_Id", "Sub_Name", "Faculty_Name", "Emp_Id"]
    
    if column not in valid_columns:
        print(f"Error: Invalid column name '{column}'.")
        return []

    query = f"SELECT * FROM subjects WHERE {column} = %s"
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
    
# .......................update function..................................................
# ..............................................................................................

def make_set_clause(subject):
  set_clause = []
  for key, val in subject.items():
    base_str = "{}={}" if key == "active" else "{}='{}'"
    set_clause.append(base_str.format(subject_column_name.get(key, key), val))
  return ",".join(set_clause)


def update_subject(subject, Sub_Id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    
    query_template = f"UPDATE subjects SET {make_set_clause(subject)} WHERE Sub_Id = %s"
    
    # Prepare the values tuple for placeholders in the query
    values =  (Sub_Id,)
    print(query_template)
    print(values)
    cursor.execute(query_template,values)
    cnx.commit()
    cursor.close()
    cnx.close()
    return get_by_id_subject(Sub_Id)
  else:
    print("Error : Unable to connect with Mysql")
    return {}
  


# .....................search by primary key(Sub_Id).........................................
# ..........................................................................................

def get_by_id_subject(id):
  cnx = connect_to_mysql()
  if cnx and cnx.is_connected():
    cursor = cnx.cursor()
    cursor.execute(show_subject, (id,))
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