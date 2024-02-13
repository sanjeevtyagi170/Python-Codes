import pandas as pd
with open("input.txt","r") as fl:
    lines=fl.read().split("\n")
numbers=[]
text=[]
for word in lines.split():
    numbers.append(int(word[0]))
    text.append(word[1])
df=pd.DataFrame({"numbers": numbers, "text": text})
encoded_numbers=[]
x=len(df["numbers"])
y=int(round((pow(x, 0.5045)*(1.341)),0))
for i in range(y+2):
    encoded_numbers.append(int((i*(i+1)/2)))
output=df[df["numbers"].isin(encoded_numbers)].sort_values(by="numbers")["text"].tolist()
print(" ".join(output))


