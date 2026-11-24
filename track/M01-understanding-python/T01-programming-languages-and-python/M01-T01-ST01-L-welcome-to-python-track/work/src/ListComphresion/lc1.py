lst=[1,2,3,4,5,6,7,8,9,0,11,22,33,44,55,66,77,88,99,00]
lstsqr=[n**2 for n in range(len(lst))]
print(lstsqr)


names=["Abhishek","Aleena","Ann","Anu","Athira","Athul"]
namUpper=[ch.upper() for ch in names]


#2D to 1D



matrix=[[1,2],[3,4],[5,6]]

plain=[n for row in matrix for n in row]

print(plain)

#print [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]

mul=[(i,j) for i in range(1,3) for j in range(1,4)]
print(mul)