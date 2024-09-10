def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

# Get user input
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Print the Fibonacci series
print_fibonacci_series(num_terms)

