a=input("Enter a number: ") 
#This is the use of try and except block   
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")
except Exception as e:
    print(e)