def solution(S):
    count_a = 0  # Count of 'A's
    count_b = 0  # Count of 'B's after the first 'A'

    for char in S:
        if char == 'A':
            count_a += 1
        elif char == 'B' and count_a > count_b:
            count_b += 1

    deletions = count_a - count_b  # Minimum deletions needed

    return deletions

# Test cases
print(solution("BAAABAB"))  # Output: 2
print(solution("BBABAA"))   # Output: 3
print(solution("AABBBB"))   # Output: 0