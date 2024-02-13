import pandas as pd
with open("input.txt","r") as fl:
    lines=fl.read().split("\n")
numbers=[int(line.split()[0]) for line in lines]
text=[line.split()[1] for line in lines]
df=pd.DataFrame({"numbers": numbers, "text": text})
encoded_numbers=[]
x=len(df["numbers"])
y=int(round((pow(x, 0.5045)*(1.341)),0))
for i in range(y+2):
    encoded_numbers.append(int((i*(i+1)/2)))
output=df[df["numbers"].isin(encoded_numbers)].sort_values(by="numbers")["text"].tolist()
# print(" ".join(output))

print()
