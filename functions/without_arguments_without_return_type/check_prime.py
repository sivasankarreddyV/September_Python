def check_prime():
    # Get user input
    num = int(input("Enter a number to check if it is prime: "))

    # Check if the number is less than 2
    if num <= 1:
        print(f"{num} is not a prime number.")
        return
    
    # Check for factors other than 1 and itself
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return
    
    # If no factors were found
    print(f"{num} is a prime number.")

# Call the function
check_prime()

