def largestNumber(a):
    l=a[0]
    for i in range(1,len(a)):
        if a[i]>l:
            l=a[i]
    return l


a=list(map(int,input("Enter input with space : ").split()))
print(largestNumber(a))