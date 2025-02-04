# Problem 5: Calculate the factorial of a number using a for loop.

n = int(input("Enter a non-negative integer: "))  # e.g., 5

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)
