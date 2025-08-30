# Program: Check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

word = "madam"
print(f"Is '{word}' a palindrome?:", is_palindrome(word))
