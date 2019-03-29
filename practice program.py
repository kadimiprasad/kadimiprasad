class prasad:

    def __init__(self):

     global file
     file = input("enter the file name")
     global identify
     identify = input("enter the identifyword")
    def counted(self):
        c=0
        with open(file,'r') as f:
            for i in f:
                p=i.split()
                for word in p:
                    if identify==word:
                        c=c+1
        print(c)

ob=prasad()
ob.counted()