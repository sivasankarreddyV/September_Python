def is_prime():
    num = int(input("Enter a number: "))
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main program
result = is_prime()

if result:
    print("The number is prime.")
else:
    print("The number is not prime.")

