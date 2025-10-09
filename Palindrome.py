def is_palindrome_string(s):
    # Optional: Convert to lowercase for case insensitive comparison
    s = s.lower()
    return s == s[::-1]

# Usage example
print(is_palindrome_string("Racecar"))