# Program to iterate over keys and values in a dictionary

student = {
    "name": "Charlie",
    "age": 23,
    "course": "Physics"
}

# Iterating over keys
for key in student:
    print(key, ":", student[key])

# Iterating over key-value pairs
for key, value in student.items():
    print(key, ":", value)
