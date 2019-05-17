import re
k=re.compile(r"\s+")
f=open("file60.txt",)
f1=open("csv.txt","w")

while f:
    pro=f.readline()
    if not pro:
        break
    print (pro)
    p=pro.split()
    f1.write( '"'+'","'.join(p)+ '"\n')

f1.close()