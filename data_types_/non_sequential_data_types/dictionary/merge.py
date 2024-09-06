# Program to merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merging dictionaries (dict2 values overwrite dict1 where keys overlap)
merged_dict = {**dict1, **dict2}

print("Merged dictionary:", merged_dict)

