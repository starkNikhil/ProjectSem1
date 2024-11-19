import pymysql

conn = pymysql.connect(
    port=3306,
    host="localhost",       # MySQL host
    user="root",            # MySQL username
    password="Nikhil@2003",    # MySQL password
    database="projectsem1"      # Name of the database
)

cursor = conn.cursor()   # Create a cursor object to execute SQL queries
print(cursor)

# Create Employees table first
cursor.execute("""
CREATE TABLE Employees (
    Emp_Id INT,
    Name VARCHAR(20) NOT NULL,
    Contact_Number VARCHAR(15) NOT NULL,
    Email_Id VARCHAR(20) NOT NULL,
    PRIMARY KEY(Emp_Id)
);
""")

# Create Student table
cursor.execute("""
CREATE TABLE Student (
    Std_Id INT,
    Name VARCHAR(25) NOT NULL,
    Email_Id VARCHAR(24) NOT NULL,
    Date_Of_Birth DATE NOT NULL,
    Guardian_Name VARCHAR(30) NOT NULL,
    Nationality VARCHAR(20) NOT NULL,
    Gender ENUM('M','F') NOT NULL,
    Contact_Number VARCHAR(15) NOT NULL,
    Address VARCHAR(35) NOT NULL,
    PRIMARY KEY (Std_Id)
);
""")

# Create Subjects table (Dependent on Subject_Marks and Employees)
cursor.execute("""
CREATE TABLE Subjects (
    Sub_Id INT NOT NULL,
    Sub_Name VARCHAR(20) NOT NULL,
    Faculty_Name VARCHAR(29) NOT NULL,
    Emp_Id INT NOT NULL,
    FOREIGN KEY (Emp_Id) REFERENCES Employees (Emp_Id),
    PRIMARY KEY (Sub_Id)
);
""")


# Create Subject_Marks table (Dependent on Student)
cursor.execute("""
CREATE TABLE Subject_Marks (
    SR_No INT NOT NULL,
    Std_Id INT NOT NULL,
    Sub_Id INT,
    Marks INT NOT NULL,
    Grade VARCHAR(7) NOT NULL,
    Semester VARCHAR(5) NOT NULL,
    PRIMARY KEY (SR_No),
    FOREIGN KEY (Sub_Id) REFERENCES Subjects (Sub_Id),
    FOREIGN KEY (Std_Id) REFERENCES Student (Std_Id)
);
""")
 
cursor.execute("""
CREATE TABLE Audit_Log (
    Log_Id INT AUTO_INCREMENT PRIMARY KEY,
    Table_Name VARCHAR(30),
    Operation_Type VARCHAR(10),
    Affected_Keys VARCHAR(50),
    Old_Data TEXT,
    New_Data TEXT,
    Operation_Time DATETIME DEFAULT CURRENT_TIMESTAMP
);
            """)

# -- Triggers for Employee table 
# -- Insert Trigger
cursor.execute(
   """
DELIMITER //
CREATE TRIGGER after_employees_insert
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Employees', 
        'INSERT', 
        CONCAT('Emp_Id: ', NEW.Emp_Id), 
        NULL, 
        CONCAT('Emp_Id: ', NEW.Emp_Id, ', Name: ', NEW.Name, ', Contact: ', NEW.Contact_Number, ', Email: ', NEW.Email_Id)
    );
END;
//
DELIMITER ;
""" 
)

# -- Update Trigger
cursor.execute("""
DELIMITER //
CREATE TRIGGER after_employees_update
AFTER UPDATE ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Employees', 
        'UPDATE', 
        CONCAT('Emp_Id: ', OLD.Emp_Id), 
        CONCAT('Emp_Id: ', OLD.Emp_Id, ', Name: ', OLD.Name, ', Contact: ', OLD.Contact_Number, ', Email: ', OLD.Email_Id),
        CONCAT('Emp_Id: ', NEW.Emp_Id, ', Name: ', NEW.Name, ', Contact: ', NEW.Contact_Number, ', Email: ', NEW.Email_Id)
    );
END;
//
DELIMITER ;
""")

# -- Delete Trigger
cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_employees_delete
AFTER DELETE ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Employees', 
        'DELETE', 
        CONCAT('Emp_Id: ', OLD.Emp_Id), 
        CONCAT('Emp_Id: ', OLD.Emp_Id, ', Name: ', OLD.Name, ', Contact: ', OLD.Contact_Number, ', Email: ', OLD.Email_Id),
        NULL
    );
END;
//
DELIMITER ;
"""
)

# -- Triggers for Student Table
# -- Insert Trigger

cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_student_insert
AFTER INSERT ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Student',
        'INSERT',
        CONCAT('Std_Id: ', NEW.Std_Id),
        NULL,
        CONCAT('Std_Id: ', NEW.Std_Id, ', Name: ', NEW.Name, ', Email: ', NEW.Email_Id, ', DOB: ', NEW.Date_Of_Birth, ', Guardian: ', NEW.Guardian_Name, ', Nationality: ', NEW.Nationality, ', Gender: ', NEW.Gender, ', Contact: ', NEW.Contact_Number, ', Address: ', NEW.Address)
    );
END;
//
DELIMITER ;
""")

# -- Update Trigger
cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_student_update
AFTER UPDATE ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Student',
        'UPDATE',
        CONCAT('Std_Id: ', OLD.Std_Id),
        CONCAT('Std_Id: ', OLD.Std_Id, ', Name: ', OLD.Name, ', Email: ', OLD.Email_Id, ', DOB: ', OLD.Date_Of_Birth, ', Guardian: ', OLD.Guardian_Name, ', Nationality: ', OLD.Nationality, ', Gender: ', OLD.Gender, ', Contact: ', OLD.Contact_Number, ', Address: ', OLD.Address),
        CONCAT('Std_Id: ', NEW.Std_Id, ', Name: ', NEW.Name, ', Email: ', NEW.Email_Id, ', DOB: ', NEW.Date_Of_Birth, ', Guardian: ', NEW.Guardian_Name, ', Nationality: ', NEW.Nationality, ', Gender: ', NEW.Gender, ', Contact: ', NEW.Contact_Number, ', Address: ', NEW.Address)
    );
END;
//
DELIMITER ;
"""
)

# -- Delete Trigger

cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_student_delete
AFTER DELETE ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Student',
        'DELETE',
        CONCAT('Std_Id: ', OLD.Std_Id),
        CONCAT('Std_Id: ', OLD.Std_Id, ', Name: ', OLD.Name, ', Email: ', OLD.Email_Id, ', DOB: ', OLD.Date_Of_Birth, ', Guardian: ', OLD.Guardian_Name, ', Nationality: ', OLD.Nationality, ', Gender: ', OLD.Gender, ', Contact: ', OLD.Contact_Number, ', Address: ', OLD.Address),
        NULL
    );
END;
//
DELIMITER ;
"""
)

# -- Triggers for Subjects

cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_subjects_insert
AFTER INSERT ON Subjects
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Subjects',
        'INSERT',
        CONCAT('Sub_Id: ', NEW.Sub_Id),
        NULL,
        CONCAT('Sub_Id: ', NEW.Sub_Id, ', Sub_Name: ', NEW.Sub_Name, ', Faculty_Name: ', NEW.Faculty_Name, ', Emp_Id: ', NEW.Emp_Id)
    );
END;
//
DELIMITER ;
"""
)

cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_subjects_update
AFTER UPDATE ON Subjects
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Subjects',
        'UPDATE',
        CONCAT('Sub_Id: ', OLD.Sub_Id),
        CONCAT('Sub_Id: ', OLD.Sub_Id, ', Sub_Name: ', OLD.Sub_Name, ', Faculty_Name: ', OLD.Faculty_Name, ', Emp_Id: ', OLD.Emp_Id),
        CONCAT('Sub_Id: ', NEW.Sub_Id, ', Sub_Name: ', NEW.Sub_Name, ', Faculty_Name: ', NEW.Faculty_Name, ', Emp_Id: ', NEW.Emp_Id)
    );
END;
//
DELIMITER ;
"""
)


cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_subjects_delete
AFTER DELETE ON Subjects
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Subjects',
        'DELETE',
        CONCAT('Sub_Id: ', OLD.Sub_Id),
        CONCAT('Sub_Id: ', OLD.Sub_Id, ', Sub_Name: ', OLD.Sub_Name, ', Faculty_Name: ', OLD.Faculty_Name, ', Emp_Id: ', OLD.Emp_Id),
        NULL
    );
END;
//
DELIMITER ;

"""
)

# -- Triggers for Subject_Marks Table

cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_subject_marks_insert
AFTER INSERT ON Subject_Marks
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Subject_Marks',
        'INSERT',
        CONCAT('SR_No: ', NEW.SR_No),
        NULL,
        CONCAT('SR_No: ', NEW.SR_No, ', Std_Id: ', NEW.Std_Id, ', Sub_Id: ', NEW.Sub_Id, ', Marks: ', NEW.Marks, ', Grade: ', NEW.Grade, ', Semester: ', NEW.Semester)
    );
END;
//
DELIMITER ;

"""
)

cursor.execute("""
DELIMITER //
CREATE TRIGGER after_subject_marks_update
AFTER UPDATE ON Subject_Marks
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Subject_Marks',
        'UPDATE',
        CONCAT('SR_No: ', OLD.SR_No),
        CONCAT('SR_No: ', OLD.SR_No, ', Std_Id: ', OLD.Std_Id, ', Sub_Id: ', OLD.Sub_Id, ', Marks: ', OLD.Marks, ', Grade: ', OLD.Grade, ', Semester: ', OLD.Semester),
        CONCAT('SR_No: ', NEW.SR_No, ', Std_Id: ', NEW.Std_Id, ', Sub_Id: ', NEW.Sub_Id, ', Marks: ', NEW.Marks, ', Grade: ', NEW.Grade, ', Semester: ', NEW.Semester)
    );
END;
//
DELIMITER ;

""")

cursor.execute(
    """
DELIMITER //
CREATE TRIGGER after_subject_marks_delete
AFTER DELETE ON Subject_Marks
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Table_Name, Operation_Type, Affected_Keys, Old_Data, New_Data)
    VALUES (
        'Subject_Marks',
        'DELETE',
        CONCAT('SR_No: ', OLD.SR_No),
        CONCAT('SR_No: ', OLD.SR_No, ', Std_Id: ', OLD.Std_Id, ', Sub_Id: ', OLD.Sub_Id, ', Marks: ', OLD.Marks, ', Grade: ', OLD.Grade, ', Semester: ', OLD.Semester),
        NULL
    );
END;
//
DELIMITER ;
"""
)

cursor.execute(
    """
CREATE VIEW EmployeeSubjectsView AS
SELECT 
    E.Emp_Id AS Employee_ID,
    E.Name AS Employee_Name,
    E.Contact_Number AS Employee_Contact,
    E.Email_Id AS Employee_Email,
    S.Sub_Id AS Subject_ID,
    S.Sub_Name AS Subject_Name,
    S.Faculty_Name AS Faculty_Name
FROM 
    Employees E
INNER JOIN 
    Subjects S
ON 
    E.Emp_Id = S.Emp_Id;"""
)

cursor.execute(
    """
CREATE VIEW StudentSubjectMarksView AS
SELECT 
    S.Std_Id AS Roll_Number,
    S.Name AS Student_Name,
    Sub.Sub_Id AS Subject_ID,
    Sub.Sub_Name AS Subject_Name,
    Sub.Faculty_Name AS Faculty_Name,
    SM.Marks AS Marks_Obtained,
    SM.Grade AS Grade,
    SM.Semester AS Semester
FROM 
    Student S
JOIN 
    Subject_Marks SM ON S.Std_Id = SM.Std_Id
JOIN 
    Subjects Sub ON SM.Sub_Id = Sub.Sub_Id;"""
)
# Create Attendance table (Dependent on Student and Subject_Marks)
# cursor.execute("""
# CREATE TABLE Attendance (
#     Std_id INT NOT NULL,
#     Sub_Id INT NOT NULL,
#     No_Of_Classes INT NOT NULL,
#     Percentage_Of_Attendance INT NOT NULL,
#     FOREIGN KEY (Sub_Id) REFERENCES Subject_Marks (Sub_Id),
#     FOREIGN KEY (Std_Id) REFERENCES Student (Std_Id)
# );
# """)

# Create Course_Total_Classes table (Dependent on Subject_Marks)
# cursor.execute("""
# CREATE TABLE Course_Total_Classes (
#     Course VARCHAR(20) NOT NULL,
#     Sub_Id INT NOT NULL,
#     No_Of_Theory_Classes INT NOT NULL,
#     No_Of_Lab_Classes INT NOT NULL,
#     Total_No_Of_Classes INT NOT NULL,
#     FOREIGN KEY (Sub_Id) REFERENCES Subject_Marks (Sub_Id)
# );
# """)

# Create Std_login table (Dependent on Student)
# cursor.execute("""
# CREATE TABLE Std_login (
#     Std_Id INT NOT NULL,
#     Password VARCHAR(20) NOT NULL,
#     Std_Name VARCHAR(20) NOT NULL,
#     FOREIGN KEY (Std_Id) REFERENCES Student (Std_Id)
# );
# """)


# Create Admins table
# cursor.execute("""
# CREATE TABLE Admins (
#     Admin_Id INT,
#     # User_Name VARCHAR(50) NOT NULL,
#     Password VARCHAR(20) NOT NULL,
#     PRIMARY KEY(Admin_Id)
# );
# """)

conn.commit()
conn.close()
