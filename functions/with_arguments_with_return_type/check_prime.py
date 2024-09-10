def get_number_and_check_prime():
    number = int(input("Enter a number: "))
    return is_prime(number)

def main():
    # Example usage of the different functions
    print("No arguments, no return type:")
    print_prime_status()

    print("\nWith arguments, no return type:")
    number = int(input("Enter a number: "))
    check_prime_and_print(number)

    print("\nWith arguments, with return type:")
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    print("\nNo arguments, with return type:")
    if get_number_and_check_prime():
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")

if __name__ == "__main__":
    main()
