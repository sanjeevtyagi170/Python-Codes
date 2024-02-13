import pandas as pd
with open("input.txt","r") as fl:
    lines=fl.read().split("\n")
numbers=[]
text=[]
for line in lines:
    word=line.split()
    numbers.append(int(word[0]))
    text.append(word[1])
df=pd.DataFrame({"numbers": numbers, "text": text})

encoded_numbers=[]
x=len(df["numbers"])
y=int(round((pow(x, 0.7)*(0.5)),0))+2
for i in range(y):
    seq=int((i*(i+1)/2))
    encoded_numbers.append(seq)
output=df[df["numbers"].isin(encoded_numbers)].sort_values(by="numbers")["text"].tolist()
print(" ".join(output))


