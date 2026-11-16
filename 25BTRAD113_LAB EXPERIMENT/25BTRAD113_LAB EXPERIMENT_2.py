# ----------------------------------------------------------------------
# Experiment 5: Number guessing game
# ----------------------------------------------------------------------
def experiment_5(low=1, high=100):
    number = random.randint(low, high)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print(f"Guess a number between {low} and {high}")

    while True:
        guess = read_int("Enter your guess: ")
        if not low <= guess <= high:
            print(f"Please guess between {low} and {high}.")
            continue
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break


# ----------------------------------------------------------------------
# Experiment 6: Prime number and factorial
# ----------------------------------------------------------------------
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


def experiment_6():
    print("--- Prime Number Program ---")
    n = read_int("Enter a number: ")
    print(n, "is a Prime Number" if is_prime(n) else "is not a Prime Number")

    print("\n--- Factorial Program ---")
    n = read_int("Enter a number: ")
    try:
        print("Factorial of", n, "is", factorial(n))
    except ValueError as err:
        print("Error:", err)


# ----------------------------------------------------------------------
# Experiment 7: Fibonacci series using recursion
# ----------------------------------------------------------------------
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def experiment_7():
    while True:
        terms = read_int("Enter the number of terms: ")
        if terms >= 0:
            break
        print("Please enter a non-negative number.")
    print("Fibonacci Series:")
    print(*(fibonacci(i) for i in range(terms)))
