r=int(input("Enter the number of Rows:"))
c=int(input("Enter the number of Columns:"))

for i in range(r):
    if i==0 or i==r-1:
        print("*"*c)
    else:
        print("*"+" "*(c-2)+"*")
    
    