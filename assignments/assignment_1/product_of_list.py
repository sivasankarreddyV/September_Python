#multiply all the numbers in a list.
def multiply_list(numbers):
    s=1
    for n in numbers:
        s=s*n
        print(f"multiply of the list:{s}")
        
numbers=[1,2,3,4,5,6]
multiply_list(numbers)
