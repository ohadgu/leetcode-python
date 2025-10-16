def is_bad_version(version: int) -> bool:
    # This is a mock implementation for demonstration purposes.
    # In a real scenario, this function would be provided and would check if the version is bad.
    return version >= 4  # Assume version 4 and onwards are bad for this example.

def first_bad_version(n: int) -> int:
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left