n=int(input("Enter the number of Rows: "))

for i in range(2*n):
    if i==0 or i==(2*n-1):
        print(" "*(n-1)+"*")
    else:
        if i<n:
            print(" "*(n-i-1)+"*"+" "*(2*i-1)+"*")
        else:
            k=2*n-i-1
            print(" "*(n-k-1)+"*"+" "*(2*k-1)+"*")