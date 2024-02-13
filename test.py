def decode(message_file):
    with open(message_file,"r") as fl:
        lines=fl.read().split("\n")
    numbers=[int(line.split()[0]) for line in lines]
    text=[line.split()[1] for line in lines]
    no_of_rows=len(numbers)
    times_for_loop_run=int(round((pow(no_of_rows, 0.5045)*(1.341)),0)) # did by trial and error
    encoded_numbers=[int((i*(i+1)/2)) for i in range(times_for_loop_run+2)]
    output = [text[i] for i in sorted(range(len(numbers)), key=numbers.__getitem__) if numbers[i] in encoded_numbers]
    print(" ".join(output))
    return " ".join(output)

decode("input.txt")
