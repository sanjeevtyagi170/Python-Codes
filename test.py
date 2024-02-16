def calPoints(operations):
        operator=['+','C','D']
        stack=[]
        for i in operations:
            if i in operator:
                if i=='C':
                    stack.pop()
                elif i=='D':
                    last_element=stack[-1]
                    stack.append(int(last_element)*2)
                elif i=='+':
                    last_element=stack[-1]
                    second_last_element=stack[-2]
                    stack.append(int(last_element)+int(second_last_element))
            else:
                stack.append(int(i))
        return sum(stack)
ops = ["5","2","C","D","+"]
print(calPoints(ops))