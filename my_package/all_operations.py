import math
import datetime
import time
import random
import string
import uuid


def get_choice(prompt="Enter your choice: "):
    """Return the menu choice as an int, or -1 if the input isn't a number."""
    try:
        return int(input(prompt))
    except ValueError:
        return -1


# ========== MATHS OPERATIONS ==========
def factorial():
    try:
        n = int(input("Enter number for factorial: "))
        print(f"Factorial of {n} is: {math.factorial(n)}")
    except ValueError:
        print("Invalid Input!")


def compound_interest():
    try:
        p = float(input("Enter Principal (P): "))
        r = float(input("Enter Rate (R): "))
        t = float(input("Enter Time (T): "))
        amount = p * pow(1 + r / 100, t)
        print(f"Total Amount: {amount:.2f}")
        print(f"Compound Interest: {amount - p:.2f}")
    except ValueError:
        print("Something went wrong!")


def trigonometry():
    try:
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)
        print(f"sin({angle}) = {math.sin(rad)}")
        print(f"cos({angle}) = {math.cos(rad)}")
        print(f"tan({angle}) = {math.tan(rad)}")
    except ValueError:
        print("Invalid Input!")


def area():
    try:
        r = float(input("Enter radius: "))
        print(f"Area of Circle: {math.pi * r * r}")
    except ValueError:
        print("Invalid Input!")


def math_operation():
    while True:
        print("\nSelect a maths operation: ")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of circle")
        print("5. Back to Main Menu")
        choice = get_choice("\nEnter your choice: ")
        if choice == 1:
            factorial()
        elif choice == 2:
            compound_interest()
        elif choice == 3:
            trigonometry()
        elif choice == 4:
            area()
        elif choice == 5:
            break
        else:
            print("Invalid Input!")
        print("==============================")


# ========== DATETIME OPERATIONS ==========
def display_current():
    now = datetime.datetime.now()
    print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def date_difference():
    try:
        d1 = input("\nEnter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        diff = abs((date2 - date1).days)
        print(f"Difference: {diff} days")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD")


def format_date():
    try:
        d = input("\nEnter date (YYYY-MM-DD): ")
        date_obj = datetime.datetime.strptime(d, "%Y-%m-%d")
        print(f"DD/MM/YYYY: {date_obj.strftime('%d/%m/%Y')}")
        print(f"Month Day, Year: {date_obj.strftime('%B %d, %Y')}")
    except ValueError:
        print("Invalid date!")


def stopwatch():
    input("\nPress Enter to start stopwatch...")
    start = time.time()
    input("Press Enter to stop stopwatch...")
    end = time.time()
    print(f"Elapsed Time: {round(end - start, 2)} seconds")


def countdown_timer():
    try:
        sec = int(input("\nEnter seconds for countdown: "))
        print("Countdown starts...")
        while sec > 0:
            print(f"{sec}...", end="\r")
            time.sleep(1)
            sec -= 1
        print("Time's up!        ")
    except ValueError:
        print("Invalid Input!")


def datetime_operation():
    while True:
        print("\nDatetime and Time Operations: ")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = get_choice()
        if choice == 1:
            display_current()
        elif choice == 2:
            date_difference()
        elif choice == 3:
            format_date()
        elif choice == 4:
            stopwatch()
        elif choice == 5:
            countdown_timer()
        elif choice == 6:
            break
        else:
            print("Enter a valid Input!")
        print("==============================")


# ========== RANDOM OPERATIONS ==========
def generate_number():
    try:
        start = int(input("Enter start range: "))
        end = int(input("Enter end range: "))
        print(f"Random Number: {random.randint(start, end)}")
    except ValueError:
        print("Invalid input!")


def generate_list():
    try:
        n = int(input("Enter length of list: "))
        rand_list = [random.randint(1, 100) for _ in range(n)]
        print(f"Random List: {rand_list}")
    except ValueError:
        print("Invalid input!")


def create_password():
    try:
        length = int(input("\nEnter password length: "))
        chars = string.ascii_letters + string.digits + "@#$!&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input!")


def generate_otp():
    otp = random.randint(100000, 999999)
    print(f"Generated OTP: {otp}")


def random_operation():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = get_choice()
        if choice == 1:
            generate_number()
        elif choice == 2:
            generate_list()
        elif choice == 3:
            create_password()
        elif choice == 4:
            generate_otp()
        elif choice == 5:
            break
        else:
            print("Enter a valid Input!")
        print("==============================")


# ========== UUID OPERATIONS ==========
def uuid_operation():
    while True:
        print("\nGenerate Unique Identifiers:")
        print("1. Generate UUID")
        print("2. Back to Main Menu")
        choice = get_choice()
        if choice == 1:
            print(f"\nGenerated UUID: {uuid.uuid4()}")
        elif choice == 2:
            break
        else:
            print("Enter a valid Input!")
        print("==============================")


# ========== MAIN MENU ==========
def main():
    while True:
        print("\n===== MULTI-UTILITY TOOLKIT =====")
        print("1. Maths Operations")
        print("2. Datetime and Time Operations")
        print("3. Random Data Generation")
        print("4. Unique Identifiers (UUID)")
        print("5. Exit")
        choice = get_choice()
        if choice == 1:
            math_operation()
        elif choice == 2:
            datetime_operation()
        elif choice == 3:
            random_operation()
        elif choice == 4:
            uuid_operation()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Enter a valid Input!")


if __name__ == "__main__":
    main()