def write_and_close_file():
    # Open the file in write mode
    file = open('example.txt', 'w')
    
    # Write some text to the file
    file.write("This is a test file.\n")
    file.write("Make sure to close the file after writing.\n")
    
    # Close the file
    file.close()

# Call the function
write_and_close_file()

