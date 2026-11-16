# ----------------------------------------------------------------------
# Experiment 1: Verify Python installation / setup
# ----------------------------------------------------------------------
def experiment_1():
    print("Python version :", platform.python_version())
    print("Executable     :", sys.executable)
    print("Platform       :", platform.platform())
    print("Setup OK - Python is installed and working!")


# ----------------------------------------------------------------------
# Experiment 2: Basic Python program
# ----------------------------------------------------------------------
def experiment_2():
    name = input("Enter your name: ").strip() or "Stranger"
    print("Hello", name)
    print("Python is working successfully!")


# ----------------------------------------------------------------------
# Experiment 3: Variables, operators, input/output
# ----------------------------------------------------------------------
def experiment_3():
    name = input("Enter your name: ").strip()
    age = read_int("Enter your age: ")
    print("Name =", name)
    print("Age =", age)
    print("Age after 5 years =", age + 5)


# ----------------------------------------------------------------------
# Experiment 4: Simple calculator and area calculation
# ----------------------------------------------------------------------
def experiment_4():
    a = read_number("Enter first number: ")
    b = read_number("Enter second number: ")
    print("Addition       =", fmt(a + b))
    print("Subtraction    =", fmt(a - b))
    print("Multiplication =", fmt(a * b))
    if b == 0:
        print("Division       = Error: cannot divide by zero")
    else:
        print("Division       =", a / b)

    length = read_number("Enter length: ")
    breadth = read_number("Enter breadth: ")
    if length < 0 or breadth < 0:
        print("Length and breadth cannot be negative.")
    else:
        print("Area of rectangle =", fmt(length * breadth))
