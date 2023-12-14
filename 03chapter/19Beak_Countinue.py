a= int(input("Enter the number: "))

for i in range(a):
    print(i)
    if(i==9):
        break

for i in range(a):
    if(i==9):# It will skip te value of the a
        continue
    print(i)