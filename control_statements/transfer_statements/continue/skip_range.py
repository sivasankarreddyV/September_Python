# Program to print numbers from 1 to 10, skipping 4 and 7

for i in range(1, 11):
    if i in [4, 7]:
        continue  # Skip 4 and 7
    print(i)

