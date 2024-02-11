def solution(S):
    count_a = 0  # Count of 'A's
    count_b = 0  # Count of 'B's

    for char in S:
        if char == 'A':
            count_a += 1
        else:  # char == 'B'
            count_b += 1

    deletions = min(count_a, count_b)  # Minimum deletions needed

    return deletions

# Test cases
print(solution("BAAABAB"))  # Output: 2
print(solution("BBABAA"))   # Output: 3
print(solution("AABBBB"))   # Output: 0



print(solution("BAAABAB")) #return 2
print(solution("BBABAA")) #return 
print(solution("AABBBB"))