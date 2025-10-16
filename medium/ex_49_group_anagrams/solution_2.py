def are_anagrams(s, t):
    if len(s) != len(t):
        return False

    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    return all(x == 0 for x in freq)

def group_anagrams(strs):
    anagram_list = []
    for _str in strs:
        for anagram in anagram_list:
            if are_anagrams(_str, anagram[0]):
                anagram.append(_str)
                break
        else:
            anagram_list.append([_str])
    return anagram_list

strs = ["eat","tea","tan","ate","nat","bat"]
anagram_list = group_anagrams(strs)
input("end")
