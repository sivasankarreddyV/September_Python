#to check whether a number is "Perfect" or not. 
def is_perfect_number(num):
    if num < 1:
        print("Input should be a positive integer.")
        return
    
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    
    if divisors_sum == num:
        print(f"{num} is a Perfect number.")
    else:
        print(f"{num} is not a Perfect number.")

# Example usage
number = 28
is_perfect_number(number)
