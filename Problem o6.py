# Problem 6: Generate Fibonacci series.

n_terms = int(input("Enter the number of terms for the Fibonacci series: "))  # e.g., 10

if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci series: [0]")
else:
    fib_series = []
    a, b = 0, 1
    for i in range(n_terms):
        fib_series.append(a)
        a, b = b, a + b
    print("Fibonacci series with", n_terms, "terms:")
    print(fib_series)
