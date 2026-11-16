# ----------------------------------------------------------------------
# Experiment 14: Bank account system using OOP
# ----------------------------------------------------------------------
class BankAccount:
    def __init__(self, acc_no, holder_name, balance=0.0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}")
        else:
            print("Transaction Failed: Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Transaction Failed: Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print("Transaction Failed: Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining Balance: ${self.__balance:.2f}")


def experiment_14():
    acc = BankAccount("ACC1001", "Sushanth", 500.0)
    acc.deposit(200.0)
    acc.withdraw(150.0)
    acc.withdraw(700.0)


# ----------------------------------------------------------------------
# Experiment 15: Library management system
# ----------------------------------------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def issue_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' issued successfully.")
        else:
            print(f"Book '{self.title}' is currently unavailable.")

    def return_book(self):
        if self.is_available:
            print(f"Book '{self.title}' was not issued, so it can't be returned.")
        else:
            self.is_available = True
            print(f"Book '{self.title}' returned successfully.")


def experiment_15():
    b1 = Book("Python Crash Course", "Eric Matthes")
    b1.issue_book()
    b1.issue_book()
    b1.return_book()


# ----------------------------------------------------------------------
# Experiment 16: Dice simulator using the random module
# ----------------------------------------------------------------------
def roll_dice(num_dice, rolls=3):
    if num_dice < 1 or rolls < 1:
        print("Number of dice and rolls must be at least 1.")
        return
    print(f"\nSimulating {rolls} rolls with {num_dice} dice:")
    for i in range(1, rolls + 1):
        outcomes = [random.randint(1, 6) for _ in range(num_dice)]
        print(f"Roll {i}: Outcomes = {outcomes} | Total = {sum(outcomes)}")


def experiment_16():
    random.seed(42)  # fixed seed = reproducible output; remove for truly random rolls
    roll_dice(num_dice=2, rolls=3)


# ----------------------------------------------------------------------
# Main menu
# ----------------------------------------------------------------------
EXPERIMENTS = {
    1: ("Check Python setup", experiment_1),
    2: ("Basic Python program", experiment_2),
    3: ("Variables, operators, input/output", experiment_3),
    4: ("Calculator and area", experiment_4),
    5: ("Number guessing game", experiment_5),
    6: ("Prime number and factorial", experiment_6),
    7: ("Fibonacci using recursion", experiment_7),
    8: ("Contact book", experiment_8),
    9: ("Student grading system", experiment_9),
    10: ("Word frequency counter", experiment_10),
    11: ("Log file reader", experiment_11),
    12: ("Student data manager (files)", experiment_12),
    13: ("CSV payroll system", experiment_13),
    14: ("Bank account (OOP)", experiment_14),
    15: ("Library management (OOP)", experiment_15),
    16: ("Dice simulator", experiment_16),
}


def main():
    while True:
        print("\n========== PYTHON LAB EXPERIMENTS ==========")
        for num, (title, _) in EXPERIMENTS.items():
            print(f"{num:>2}. {title}")
        print(" 0. Exit")
        try:
            choice = int(input("Enter experiment number: "))
        except ValueError:
            print("Please enter a number from 0 to 16.")
            continue
        if choice == 0:
            print("Goodbye!")
            break
        if choice in EXPERIMENTS:
            title, func = EXPERIMENTS[choice]
            print(f"\n----- Experiment {choice}: {title} -----")
            func()
        else:
            print("Please enter a number from 0 to 16.")


if __name__ == "__main__":
    main()
