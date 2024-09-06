# Program to demonstrate set operations: union, intersection, difference

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a.union(set_b)
print("Union:", union_set)

# Intersection
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

# Difference
difference_set = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference_set)

