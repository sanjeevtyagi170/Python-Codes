A = [1, 3, 6, 4, 1, 2]
A=sorted(set(A))
# A = [1,2,3,4,6]
not_occur=[]
for i in range(len(A)-1):
    if A[i+1]!=A[i]+1:
        x=A[i]+1
        not_occur.append(x)
print(min(not_occur))