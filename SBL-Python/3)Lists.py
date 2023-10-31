# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

while True:
    print("Menu:")
    print("1. Add elements to lists and classify as even or odd")
    print("2. Merge and sort the two lists")
    print("3. Update and delete elements in the list")
    print("4. Find max and min elements in the list")
    print("5. Add names to the existing number list and check for 'python'")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Step 2: Take the number of elements
        num_elements = int(input("Enter the number of elements: "))

        # Step 3: Take elements one by one and classify as even or odd
        for _ in range(num_elements):
            num = int(input("Enter an element: "))
            if num % 2 == 0:
                even_numbers.append(num)
            else:
                odd_numbers.append(num)

        print("Even numbers:", even_numbers)
        print("Odd numbers:", odd_numbers)

    elif choice == '2':
        # Step 6: Merge and sort the two lists
        merged_list = even_numbers + odd_numbers
        merged_list.sort()
        print("Merged and sorted list:", merged_list)

    elif choice == '3':
        # Step 7: Update and delete elements in the list
        index = int(input("Enter the index of the element to update: "))
        new_value = int(input("Enter the new value: "))
        if index >= 0 and index < len(merged_list):
            merged_list[index] = new_value

        index_to_delete = int(input("Enter the index to delete: "))
        if index_to_delete >= 0 and index_to_delete < len(merged_list):
            del merged_list[index_to_delete]

        print("Updated list:", merged_list)

    elif choice == '4':
        # Step 8: Find max and min elements in the list
        if merged_list:
            max_num = max(merged_list)
            min_num = min(merged_list)
            print(f"Maximum number: {max_num}")
            print(f"Minimum number: {min_num}")
        else:
            print("List is empty.")

    elif choice == '5':
        # Step 5: Add names to the existing number list and check for 'python'
        names = input("Enter names separated by spaces: ").split()
        merged_list.extend(names)
        if 'python' in merged_list:
            print("'python' is present in the list.")
        else:
            print("'python' is not present in the list.")

    elif choice == '6':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")
