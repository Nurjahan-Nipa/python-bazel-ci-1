"""String utility functions."""

def reverse_string(s):
    """Returns the reversed string."""
    return s[::-1]

def is_palindrome(s):
    """Checks if the string is a palindrome."""
    return s == s[::-1]

def count_vowels(s):
    """Returns the count of vowels in a string."""
    return sum(1 for char in s.lower() if char in "aeiou")
