def can_construct(ransom_note, magazine):
    if len(ransom_note) > len(magazine):
        return False

    freq = [0] * 26
    for x in ransom_note:
        freq[ord(x) - ord('a')] += 1

    for x in magazine:
        freq[ord(x) - ord('a')] -= 1

    return all(x <= 0 for x in freq)

ans = can_construct('aa', 'aab')
print(ans)
