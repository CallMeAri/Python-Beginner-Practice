word = input("Enter word ")
print(f"Original Word is :",word)
x = list(word)


for i in x[0::2]:
    print(i)
