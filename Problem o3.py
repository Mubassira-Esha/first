# Problem 3: Sum of numbers between a given lower and upper bound 

lower = int(input("Enter the lower bound (e.g., 50): "))
upper = int(input("Enter the upper bound (e.g., 100): "))

total_sum = 0
for num in range(lower, upper + 1):
    if num % 3 == 0 and num % 5 != 0:
        total_sum += num

print("Sum of numbers between", lower, "and", upper,
      "divisible by 3 and not divisible by 5:", total_sum)
