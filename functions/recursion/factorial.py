def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

def main():
    # Get user input
    num = int(input("Enter a number to find its factorial: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Call the factorial function and print the result
        result = factorial(num)
        print(f"Factorial of {num} is {result}")

# Call the main function
main()

