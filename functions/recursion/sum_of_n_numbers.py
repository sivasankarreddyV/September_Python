def sum_of_numbers(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: sum of numbers is n plus sum of numbers from n-1
    else:
        return n + sum_of_numbers(n - 1)

def main():
    # Get user input
    n = int(input("Enter a positive integer: "))

    # Check for non-positive input
    if n < 0:
        print("Please enter a positive integer.")
    else:
        # Calculate the sum using recursion
        total_sum = sum_of_numbers(n)
        print(f"Sum of the first {n} natural numbers is: {total_sum}")

# Call the main function
main()

