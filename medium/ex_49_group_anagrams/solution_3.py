def group_anagrams(strs):
    anagram_dict = {}
    for _str in strs:
        key = ''.join(sorted(_str))
        if key in anagram_dict:
            anagram_dict[key].append(_str)
        else:
            anagram_dict[key] = [_str]
    return list(anagram_dict.values())


strs = ["eat","tea","tan","ate","nat","bat"]
anagram_list = group_anagrams(strs)
input("end")
