import pandas as pd
df=pd.DataFrame({
    "country":["USA","India","UK","Germany","Australia"],
    "sales":[20000,25000,21000,8000,100000]
})
for i,row in df.iterrows():
    if row["country"]=="India":
        df["rank"]="1"
    else:
        df["rank"]="0"
print(df)

# def calPoints(operations):
#         operator=['+','C','D']
#         stack=[]
#         for i in operations:
#             if i in operator:
#                 if i=='C':
#                     stack.pop()
#                 elif i=='D':
#                     last_element=stack[-1]
#                     stack.append(int(last_element)*2)
#                 elif i=='+':
#                     last_element=stack[-1]
#                     second_last_element=stack[-2]
#                     stack.append(int(last_element)+int(second_last_element))
#             else:
#                 stack.append(int(i))
#         return sum(stack)
# ops = ["5","2","C","D","+"]
# print(calPoints(ops))