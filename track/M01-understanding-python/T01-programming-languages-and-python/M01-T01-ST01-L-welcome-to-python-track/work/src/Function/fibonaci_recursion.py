def fibonaci(count,a=0,b=1):
    if count<=0:
        return
    print(a,end=" ")
    fibonaci(count-1,b,a+b)

fibonaci(10)