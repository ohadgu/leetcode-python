def is_palindrome(s: str):
    clean_s = [c.lower() for c in s if c.isalnum()]
    return clean_s == clean_s[::-1]
