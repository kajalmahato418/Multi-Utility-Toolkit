import my_package.file_operations as fo
import my_package.all_operations as ao
import math

while True:
    print("\n=============================")
    print("Welcome to Multi-Utility Toolkit")
    print("=============================")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        ao.datetime_operation()
    elif choice == '2':
        ao.math_operation()
    elif choice == '3':
        ao.random_operation()
    elif choice == '4':
        ao.uuid_operation()
    elif choice == '5':
        fo.file_operation()
    elif choice == '6':
        print("\nAttributes of math module:")
        print(dir(math))
    elif choice == '7':
        print("Thank you for using the Multi-Utility Toolkit!")
        break
    else:
        print("Enter a valid Input!")