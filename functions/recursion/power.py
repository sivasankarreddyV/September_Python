def power(base, exponent):
    # Base case: any number raised to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: base^exponent = base * base^(exponent-1)
    return base * power(base, exponent - 1)

def main():
    # Get user input
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    
    # Calculate power using recursion
    result = power(base, exponent)
    
    # Print the result
    print(f"{base} raised to the power of {exponent} is {result}")

# Call the main function
main()

