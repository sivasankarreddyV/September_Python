def read_file():
    try:
        # Open the file in read mode
        with open('example.txt', 'r') as file:
            # Read the entire content of the file
            content = file.read()
            # Print the content
            print(content)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("The file 'example.txt' was not found.")

# Call the function to read and print the file
read_file()

