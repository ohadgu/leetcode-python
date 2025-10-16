def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = [0] * 26  # Assuming the strings contain only lowercase letters a-z
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    return all(x == 0 for x in freq)

    # for count in freq:
    #     if count != 0:
    #         return False
    #
    # return True


s = "abba"
t = "baba"
print(is_anagram(s, t))