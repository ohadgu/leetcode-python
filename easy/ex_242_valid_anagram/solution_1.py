from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

s = "abba"
t = "baba"

print(is_anagram(s, t))