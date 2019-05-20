class rotate:
    def Method(self,word,rotation):
        li = list(str(word))
        outputString = ''
        for x in li:
            outputString = outputString +chr(ord(x)+rotation)
        print("The Output String is : ",outputString)
    def getData(self):
        word = str(input("Enter the String : "))
        amt = int(input("Enter the Amount of Rotation : "))
        obj = rotate()
        obj.rotate(word,amt)
rotate.getData()
