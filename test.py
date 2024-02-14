def foo(i,x=[]):  # Create a new list inside the function
  x.append(i)
  return x

for i in range(2):
  print(foo(i))