import re
class Stringslice:
    def slice(self,line):
        temp = line
        if len(line)>0:
             line = line[::-1]
             print "The reverse word",line
        else:
            print "Given string has zero length"
        if temp == line:
             print "The given String is palindrome"
obj = Stringslice()
input =raw_input("Enter the string")
obj.slice(re.sub('','', input))


