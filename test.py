import pandas as pd
def decode(message_file):
    with open(message_file,"r") as fl:
        lines=fl.read().split("\n")
    numbers=[int(line.split()[0]) for line in lines]
    text=[line.split()[1] for line in lines]
    dataframe=pd.DataFrame({"numbers": numbers, "text": text})
    no_of_rows=dataframe.shape[0]
    times_for_loop_run=int(round((pow(no_of_rows, 0.5045)*(1.341)),0)) # did by trial and error
    encoded_numbers=[int((i*(i+1)/2)) for i in range(times_for_loop_run+2)]
    output=dataframe[dataframe["numbers"].isin(encoded_numbers)].sort_values(by="numbers")["text"].tolist()
    print(" ".join(output))
    return " ".join(output)

decode("input.txt")

dictionary={"numbers": numbers, "text": text}
print(dictionary["numbers"])