# Initialize an empty list of tuples to store student information
student_data = []

while True:
    print("Menu:")
    print("1. Add student data (Roll No, Name, Subject Marks)")
    print("2. Display student data for students named 'Python'")
    print("3. Demonstrate Nested tuple and sort nested tuple")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Step 3: Accept student data as a tuple and add it to the list
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks1 = float(input("Enter Subject 1 Marks: "))
        marks2 = float(input("Enter Subject 2 Marks: "))
        marks3 = float(input("Enter Subject 3 Marks: "))

        student_tuple = (roll_no, name, marks1, marks2, marks3)
        student_data.append(student_tuple)

    elif choice == '2':
        # Step 5: Display student data for students named 'Python'
        python_students = [student for student in student_data if 'Python' in student[1]]
        if python_students:
            print("Student data for students named 'Python':")
            for student in python_students:
                print(f"Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2:]}")
        else:
            print("No students named 'Python' found.")

    elif choice == '3':
        # Step 6: Sort student data by name
        sorted_student_data = sorted(student_data, key=lambda x: x[1])
        print("Sorted student data by name:")
        for student in sorted_student_data:
            print(f"Roll No: {student[0]}, Name: {student[1]}, Marks: {student[2:]}")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
