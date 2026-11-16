# ----------------------------------------------------------------------
# Task 1: Print name, branch and college on separate lines
# ----------------------------------------------------------------------
def task_1():
    print(STUDENT_NAME)
    print("Computer Science")
    print(COLLEGE_NAME)


# ----------------------------------------------------------------------
# Task 2: Print a block of stars (3 rows x 7 stars, as in the output)
# ----------------------------------------------------------------------
def task_2():
    for _ in range(3):
        print("*" * 7)


# ----------------------------------------------------------------------
# Task 3: Print a message
# ----------------------------------------------------------------------
def task_3():
    print("Python is Easy")


# ----------------------------------------------------------------------
# Task 4: Number triangle
# ----------------------------------------------------------------------
def task_4():
    for i in range(1, 6):
        print("".join(str(n) for n in range(1, i + 1)))


# ----------------------------------------------------------------------
# Task 5: Escape sequence \n (new line)
# ----------------------------------------------------------------------
def task_5():
    print("Computer\nScience\nEngineering")


# ----------------------------------------------------------------------
# Task 6: Escape sequence \t (tab)
# ----------------------------------------------------------------------
def task_6():
    print("Sushanth\t19\tBangalore")


# ----------------------------------------------------------------------
# Task 7: Single-line comment
# ----------------------------------------------------------------------
def task_7():
    # This program prints a welcome message.
    print("Welcome to Python")


# ----------------------------------------------------------------------
# Task 8: Multi-line comment (docstring-style)
# ----------------------------------------------------------------------
def task_8():
    """
    This is a multi-line comment.
    It explains the purpose of the program.
    This program prints a message.
    """
    print("Hello, Python!")


# ----------------------------------------------------------------------
# Task 9: Multiple comments
# ----------------------------------------------------------------------
def task_9():
    # First comment
    # Second comment
    # Third comment
    print("Hello")
    print("Welcome")
    print("Python is Easy")


# ----------------------------------------------------------------------
# Task 10: Variable
# ----------------------------------------------------------------------
def task_10():
    name = "Sushanth"
    print(name)


# ----------------------------------------------------------------------
# Task 11: Multiple variables
# ----------------------------------------------------------------------
def task_11():
    a = 10
    b = 20
    c = 30
    print(a)
    print(b)
    print(c)


# ----------------------------------------------------------------------
# Task 12: Type conversion - string to int
# ----------------------------------------------------------------------
def task_12():
    value = "100"
    number = int(value)
    print(number)
    print(type(number))


# ----------------------------------------------------------------------
# Task 13: Type conversion - int to float
# ----------------------------------------------------------------------
def task_13():
    number = 25
    result = float(number)
    print(result)
    print(type(result))


# ----------------------------------------------------------------------
# Task 14: Reading an integer
# ----------------------------------------------------------------------
def task_14():
    age = read_int("Enter your age: ")
    print("Your age is:", age)


# ----------------------------------------------------------------------
# Task 15: Sum of two numbers
# ----------------------------------------------------------------------
def task_15():
    num1 = read_int("Enter first number: ")
    num2 = read_int("Enter second number: ")
    total = num1 + num2  # 'total' instead of 'sum' so the built-in sum() isn't shadowed
    print("Sum =", total)


# ----------------------------------------------------------------------
# Task 16: Student details (name, age, CGPA)
# ----------------------------------------------------------------------
def task_16():
    name = input("Enter student's name: ").strip()
    age = read_int("Enter student's age: ")
    while True:
        cgpa = read_float("Enter student's CGPA: ")
        if 0 <= cgpa <= 10:
            break
        print("CGPA must be between 0 and 10.")
    print(f"My name is {name}. I am {age} years old and my CGPA is {cgpa}.")


# ----------------------------------------------------------------------
# Task 17: Celsius to Fahrenheit
# ----------------------------------------------------------------------
def task_17():
    celsius = read_float("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


# ----------------------------------------------------------------------
# Task 18: Even or odd
# ----------------------------------------------------------------------
def task_18():
    number = read_int("Enter number: ")
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")


# ----------------------------------------------------------------------
# Main menu
# ----------------------------------------------------------------------
TASKS = {
    1: ("Print name, branch, college", task_1),
    2: ("Star block", task_2),
    3: ("Print a message", task_3),
    4: ("Number triangle", task_4),
    5: ("New line (\\n)", task_5),
    6: ("Tab (\\t)", task_6),
    7: ("Single-line comment", task_7),
    8: ("Multi-line comment", task_8),
    9: ("Multiple comments", task_9),
    10: ("Variable", task_10),
    11: ("Multiple variables", task_11),
    12: ("String to int", task_12),
    13: ("Int to float", task_13),
    14: ("Read age", task_14),
    15: ("Sum of two numbers", task_15),
    16: ("Student details", task_16),
    17: ("Celsius to Fahrenheit", task_17),
    18: ("Even or odd", task_18),
}

NO_INPUT_TASKS = range(1, 14)  # tasks 1-13 need no keyboard input


def main():
    while True:
        print("\n========== ASSIGNMENT 1 - PYTHON BASICS ==========")
        for num, (title, _) in TASKS.items():
            print(f"{num:>2}. {title}")
        print("99. Run all tasks that need no input (1-13)")
        print(" 0. Exit")
        try:
            choice = int(input("Enter task number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 99:
            for n in NO_INPUT_TASKS:
                print(f"\n----- Task {n}: {TASKS[n][0]} -----")
                TASKS[n][1]()
        elif choice in TASKS:
            title, func = TASKS[choice]
            print(f"\n----- Task {choice}: {title} -----")
            func()
        else:
            print("Please enter a number from 0 to 18 (or 99).")


if __name__ == "__main__":
    main()
