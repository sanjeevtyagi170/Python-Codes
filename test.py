import pandas as pd
with open("input.txt","r") as fl:
    file_read=fl.read()

lines = file_read.split("\n")
data=[]
for line in lines:
    words = line.split()
    numbers = sum([int(word) for word in words if word.isdigit()])
    text = " ".join([word for word in words if not word.isdigit()])
    data.append({"numbers": numbers, "text": text})
df=pd.DataFrame(data)
print(df)