def solution(A, D):
    # Implement your solution here
    total_amount=sum(A)
    fees=5
    nom1=11
    nom2=12
    months=[]
    for amt, dt in zip(A,D):
        month =dt[5:7]
        months.append(month)
    print(months)
A=[100, 100, 100, -10]
D=['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']
solution(A,D)