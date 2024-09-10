# List of lines to write to the file
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

# Open a file in write mode
with open("example.txt", "w") as file:
    # Write the list of lines to the file
    file.writelines(lines)

print("Lines written to the file successfully.")

