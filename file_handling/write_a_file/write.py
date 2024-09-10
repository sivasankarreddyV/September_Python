# Define the filename
filename = 'example.txt'

# Open the file in write mode ('w')
with open(filename, 'w') as file:
    # Write some text to the file
    file.write('Hello, this is a test file.\n')
    file.write('Writing to files in Python is easy!\n')

print(f'Content has been written to {filename}')

