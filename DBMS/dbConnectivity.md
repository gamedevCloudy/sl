To implement MySQL/Oracle database connectivity with Python, you can use the `mysql-connector` library for MySQL and `cx_Oracle` for Oracle. Here, I'll provide an example for MySQL:

### MySQL Database Connectivity with Python
```python
import mysql.connector

# Establishing Connection
conn = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)

# Creating a Cursor
cursor = conn.cursor()

# Function to add a new record
def add_record():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    query = "INSERT INTO your_table_name (name, age) VALUES (%s, %s)"
    values = (name, age)
    
    cursor.execute(query, values)
    conn.commit()
    print("Record added successfully!")

# Function to delete a record
def delete_record():
    record_id = int(input("Enter the ID of the record to delete: "))
    
    query = "DELETE FROM your_table_name WHERE id = %s"
    value = (record_id,)
    
    cursor.execute(query, value)
    conn.commit()
    print("Record deleted successfully!")

# Function to edit a record
def edit_record():
    record_id = int(input("Enter the ID of the record to edit: "))
    new_age = int(input("Enter the new age: "))
    
    query = "UPDATE your_table_name SET age = %s WHERE id = %s"
    values = (new_age, record_id)
    
    cursor.execute(query, values)
    conn.commit()
    print("Record edited successfully!")

# Main menu for database navigation operations
while True:
    print("\nDatabase Navigation Operations:")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Edit Record")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_record()
    elif choice == '2':
        delete_record()
    elif choice == '3':
        edit_record()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Closing the connection
cursor.close()
conn.close()
```

Replace the placeholders (`your_mysql_host`, `your_mysql_user`, `your_mysql_password`, `your_database_name`, `your_table_name`) with your MySQL database credentials and table details.

### Oracle Database Connectivity with Python (using cx_Oracle)
For Oracle, you would need to install the `cx_Oracle` library. You can install it using:
```bash
pip install cx_Oracle
```

Here's a similar example for Oracle database connectivity and navigation operations:

```python
import cx_Oracle

# Establishing Connection
conn = cx_Oracle.connect("your_username/your_password@your_oracle_connection_string")

# Creating a Cursor
cursor = conn.cursor()

# Function to add a new record
def add_record():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    query = "INSERT INTO your_table_name (name, age) VALUES (:1, :2)"
    values = (name, age)
    
    cursor.execute(query, values)
    conn.commit()
    print("Record added successfully!")

# Function to delete a record
def delete_record():
    record_id = int(input("Enter the ID of the record to delete: "))
    
    query = "DELETE FROM your_table_name WHERE id = :1"
    value = (record_id,)
    
    cursor.execute(query, value)
    conn.commit()
    print("Record deleted successfully!")

# Function to edit a record
def edit_record():
    record_id = int(input("Enter the ID of the record to edit: "))
    new_age = int(input("Enter the new age: "))
    
    query = "UPDATE your_table_name SET age = :1 WHERE id = :2"
    values = (new_age, record_id)
    
    cursor.execute(query, values)
    conn.commit()
    print("Record edited successfully!")

# Main menu for database navigation operations
while True:
    print("\nDatabase Navigation Operations:")
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Edit Record")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_record()
    elif choice == '2':
        delete_record()
    elif choice == '3':
        edit_record()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Closing the connection
cursor.close()
conn.close()
```

Replace the placeholders (`your_username`, `your_password`, `your_oracle_connection_string`, `your_table_name`) with your Oracle database credentials and table details.

Make sure to handle your database credentials securely and adapt the code according to your specific requirements and table structure.