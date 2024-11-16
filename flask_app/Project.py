import pymysql

conn = pymysql.connect(
    port=3306,
    host="localhost",       # MySQL host
    user="root",            # MySQL username
    password="admin123",    # MySQL password
    database="Project"      # Name of the database
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



# Create Subject_Marks table (Dependent on Student)
cursor.execute("""
CREATE TABLE Subject_Marks (
    SR_No INT NOT NULL,
    Std_Id INT NOT NULL,
    Sub_Id INT,
    Marks INT NOT NULL,
    Grade VARCHAR(7) NOT NULL,
    Semester VARCHAR(5) NOT NULL,
    PRIMARY KEY (SR_No)
    FOREIGN KEY (Sub_Id) REFERENCES Subjects (Sub_Id)
    FOREIGN KEY (Std_Id) REFERENCES Student (Std_Id)
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
