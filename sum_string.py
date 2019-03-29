p = input("enter the list")
f = p.replace(','," ")
b = f.split()
k= 0
for i in b:
    k = k+float(i)
    print(k)