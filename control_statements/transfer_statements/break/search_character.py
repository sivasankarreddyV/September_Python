# Program to find the first occurrence of a specific character in a string

text = "Hello, World!"
search_char = "W"

for char in text:
    if char == search_char:
        print(f"Character '{search_char}' found in the text!")
        break
    print(f"Checked character '{char}', not '{search_char}'")

