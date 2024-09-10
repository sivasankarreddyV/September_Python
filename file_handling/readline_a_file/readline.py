# Open the file in read mode ('r')
with open('sample.txt', 'r') as file:
    # Read the file line by line
    while True:
        line = file.readline()
        # Break the loop if the end of the file is reached
        if not line:
            break
        # Print each line
        print(line.strip())  # .strip() is used to remove the newline character

