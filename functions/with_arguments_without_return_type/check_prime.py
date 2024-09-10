def check_prime(n):
    """Prints whether the number n is prime or not."""
    if n <= 1:
        print(f"{n} is not a prime number.")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return
    print(f"{n} is a prime number.")

def main():
    num = int(input("Enter a number: "))
    check_prime(num)

if __name__ == "__main__":
    main()

