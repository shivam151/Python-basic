def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))

f=0
s=1
def fib(n):
    global f
    global s
    if(n==0):
        return
    else:
        print(f)
        t=f+s
        f=s
        s=t
        fib(n-1)
fib (15)