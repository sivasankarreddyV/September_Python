# Program to remove elements from a set

my_set = {1, 2, 3, 4, 5}

# Removing an element
my_set.remove(3)
print("Set after removing 3:", my_set)

# Discarding an element (no error if the element is not found)
my_set.discard(6)
print("Set after discarding 6 (not present):", my_set)
