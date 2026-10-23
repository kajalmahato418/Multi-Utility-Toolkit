#create file
def create_file():
    try:
        name = input("Enter a File Name: ")
        with open (name,"x") as file:
            print("File created Succeessfully!")

    except:
        print("File already exist!")

#Add Entry
def add_entry():
    try:
        file = input("Enter a file: ")
        entry = input("Enter a new entry: ")
        with open(file,"w") as file:
            file.write(entry + "\n")
            print("Entery Added Succesfully!")
    except:
        print("Something went wrong!")

#for reading file
def read_file():
    try:
        file = input("Enter a file name: ")
        with open(file,"r") as file:
            show_entry = file.read()
            print(f"\n--- File Content ---\n{show_entry}")

    except:
        print("File not found!")

#for Appending
def append_file():
    try:
        file = input("Enter s file name: ")
        entry = input("Enter entry to append: ")
        with open(file,"a") as file:
            file.write(entry + "\n")
            print("File appended Successfully!")

    except:
        print("Something went wrong!")


#Main File Menu 
def file_operation():
    while True:
        print("\nSelect an option: ")
        print("1. Create a new file")
        print("2. Write a new file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            create_file()

        elif choice == 2:
            add_entry()

        elif choice == 3:
            read_file()

        elif choice == 4:
            append_file()

        elif choice == 5:
            break

        else:
            print("Invalid Input")



        



