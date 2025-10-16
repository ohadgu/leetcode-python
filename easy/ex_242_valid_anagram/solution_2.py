def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for val_s, val_t in zip(s, t):
        count_s[val_s] = count_s.get(val_s, 0) + 1
        count_t[val_t] = count_t.get(val_t, 0) + 1

    return count_s == count_t


s = "abba"
t = "baba"

print(is_anagram(s, t))