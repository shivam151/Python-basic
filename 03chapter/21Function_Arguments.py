#There is four types of arguments in the python
#1. Requirment argument
#2. Keyword arbitary argument
#3. Default argument
#4. Variable length argument


def avrage(a=1,b=5):
    avrage=(a+b)/2
    print( avrage)
#Default argument
avrage(2,4)#if we give one value than secound value is taken is default value

#requirment argument
def a(a,b=5):
    a=(a+b)/2
    print( a)
a(2)#If we not give the value of the a than it will give the error becouse it requirment argument

#4. Variable length argument

def avg(*number):
    sum=0
    for i in number:
        sum=sum+i
    avrage=sum/len(number)
    print(avrage)

avg(1,2,3,4,5,6,7,8,9,10)

#2. Keyword arbitary argument
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person("Rahul",age=28,city="Mumbai",mob=992670)



