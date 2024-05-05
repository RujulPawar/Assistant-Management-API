# Import the required packages
import mysql.connector
from Credentials import USER,PASSWORD

# Connect to MySQL server
db=mysql.connector.connect(host='localhost',user=USER,password=PASSWORD)

# Check if connection is established
if db.is_connected():
    print("Connection Established")

# Create cursor
cursor=db.cursor()

# Drop database if it exists
cursor.execute("drop database if exists assistantsdb")

# Create database
cursor.execute("create database assistantsdb")

# Use the created database
cursor.execute("use assistantsdb")

# Create assistants table
cursor.execute("create table assistants(id char(5) primary key not null,name varchar(50),mobile varchar(50),email varchar(50),salary varchar(10),city varchar(10),country varchar(10),department varchar(10));")

# Adding data
cursor.execute("insert into assistants values('1','Rujul Pawar','12345','rujul@gmail.com','100000','Mumbai','India','Backend');")
cursor.execute("insert into assistants values('2','Shaurya Doshi','54321','shaurya@gmail.com','10000','Mumbai','India','Frontend');")
cursor.execute("insert into assistants values('3','Samar Mhetre','12345','samar@gmail.com','1000','Mumbai','India','HR');")
cursor.execute("insert into assistants values('4','Tanishq Patel','54321','tanishq@gmail.com','100','Mumbai','India','Marketing');")
cursor.execute("insert into assistants values('5','Smit Asher','12345','smit@gmail.com','10','Mumbai','India','Sales');")

# Commit changes
db.commit()

print("Success")