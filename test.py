import pandas as pd
import numpy as np

df=pd.DataFrame({
    "country":["USA","India","UK","Germany","Australia"],
    "population":[21000,40000,20000,80000,100000]
    })

n=len(df["country"])

for i,row in df.iterrows():
    total_sum=(sum(df["population"])-row["population"])/(n-1)
    print(total_sum)

# Priority Ranking
# df=pd.DataFrame({
#     "country":["USA","India","UK","Germany","Australia"],
#     "sales":[20000,25000,21000,8000,100000]
#     })

# def ranking(df):
#     for i,row in df.iterrows():
#         if row["country"]=="India":
#             df.loc[i,"rank"]=1
#         else:
#             df.loc[i,"rank"]=0
#     return df.sort_values(by=["rank","sales"],ascending=[False,False]).drop("rank",axis=1)

# df["rank"]=np.where(df["country"]=="India",1,0)
# df=df.sort_values(by=["rank","sales"],ascending=[False,False]).drop("rank",axis=1)
# print(df)

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