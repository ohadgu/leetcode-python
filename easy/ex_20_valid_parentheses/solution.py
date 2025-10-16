def is_valid(_str):
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for par in _str:
        if par in pairs.values():
            stack.append(par)
        else:
            if not stack or stack.pop() != pairs[par]:
                return False

    return len(stack) == 0
