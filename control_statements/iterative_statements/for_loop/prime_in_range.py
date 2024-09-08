# Program to print all prime numbers between 1 and 20

for num in range(2, 21):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

