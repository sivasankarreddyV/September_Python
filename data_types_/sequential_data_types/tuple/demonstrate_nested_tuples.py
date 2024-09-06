# Program to demonstrate nested tuples

nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (4.5, 5.5, 6.5))
print("Nested tuple:", nested_tuple)

# Accessing elements from nested tuples
first_element = nested_tuple[0]
first_inner_element = nested_tuple[0][1]

print("First element of nested tuple:", first_element)
print("First inner element of first tuple:", first_inner_element)

