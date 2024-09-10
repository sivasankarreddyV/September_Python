def open_and_read_file():
    try:
        # Open the file in read mode ('r')
        file = open('example.txt', 'r')
        
        # Read the content of the file
        content = file.read()
        print("File content:\n")
        print(content)
        
    except FileNotFoundError:
        print("The file was not found. Please check the file name and path.")
    
    finally:
        # Ensure the file is closed after the operation
        file.close()
        print("\nFile closed successfully.")

# Call the function
open_and_read_file()

