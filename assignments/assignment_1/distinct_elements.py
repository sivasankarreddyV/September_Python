#distinct elements from the list
def distinct_elements(lst):
    distinct_list = list(set(lst))  
    print(f"List with distinct elements: {distinct_list}")

numbers = [1, 2, 2, 3, 4, 4, 5]
distinct_elements(numbers)

