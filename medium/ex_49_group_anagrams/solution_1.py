from collections import Counter

def group_anagrams(strs):
    anagram_list = []
    for _str in strs:
        for anagram in anagram_list:
            if Counter(anagram[0]) == Counter(_str):
                anagram.append(_str)
                break
        else:
            anagram_list.append([_str])
    return anagram_list

strs = ["eat","tea","tan","ate","nat","bat"]
anagram_list = group_anagrams(strs)
input("end")
