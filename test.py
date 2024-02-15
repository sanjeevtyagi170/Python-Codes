import pandas as pd
def foo(i,x=[]):  # Create a new list inside the function
  x.append(i)
  return x

for i in range(2):
  print(foo(i))
url="https://www.kaggle.com/datasets/wolfgang91/telecom-calls-dataset?select=ICalls+dataset.xlsx"
df=pd.read_csv(url)
print(df.head())
  