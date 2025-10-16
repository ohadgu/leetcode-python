def longest_common_prefix(strs: list[str]):
    prefix = strs[0]
    for _str in strs:
        while prefix:
            if _str.startswith(prefix):
                break
            prefix = prefix[:-1]
    return prefix