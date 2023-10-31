import sqlite3

connection = sqlite3.connect('my_database.db')

# Step 2: Create a cursor object to interact with the database
cursor = connection.cursor()

# Step 3: Define a SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    age INTEGER
)
"""
# Step 4: Execute the SQL command to create the table
cursor.execute(create_table_query)

# Function to insert a new record into the table
def insert_record(connection, cursor):
    username = input("Enter username: ")
    age = int(input("Enter age: "))
    cursor.execute("INSERT INTO users (username, age) VALUES (?, ?)", (username, age))
    connection.commit()
    print("Record inserted successfully.")


# Function to update a record in the table
def update_record(connection, cursor):
    user_id = int(input("Enter the user ID to update: "))
    new_age = int(input("Enter the new age: "))
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    connection.commit()
    print("Record updated successfully.")


# Function to retrieve records from the table
def retrieve_records(cursor):
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, Username: {record[1]}, Age: {record[2]}")

while True:
    print("\nMenu:")
    print("1. Insert a new record")
    print("2. Update a record")
    print("3. Retrieve records")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert_record(connection, cursor)
    elif choice == '2':
        update_record(connection, cursor)
    elif choice == '3':
        retrieve_records(cursor)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection
connection.close()
