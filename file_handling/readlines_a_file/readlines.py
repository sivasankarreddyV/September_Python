# Open the file in read mode
with open("example.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Print each line
for line in lines:
    print(line.strip())

