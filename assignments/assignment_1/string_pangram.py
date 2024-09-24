#to check whether a string is a pangram or not.
def is_pangram(s):
    alphabet  =set("abcdefghijklmnopqrstuvwxyz")
    input_set = set(s.lower())
    if alphabet.issubset(input_set):
        print("the string is a pangram")
    else:
        print("the string is not a pangram")
sentence="The quick brown fox jumps over the lazy dog"
is_pangram(sentence)
