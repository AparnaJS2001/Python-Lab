s=input("Enter the words")
list=[]
for x in s:
  if x in ('a','e','i','o','u'):
    list.append(x)
print(list)
