
class abcd:
     def CheckOrder(self,word):
        for i in range(len(word)-1):
             if ord(word[i])>ord(word[i+1]):
                return False
        return True
obj = abcd()
word= raw_input("Enter the string:")
Result=obj.CheckOrder(word)
if Result:
     print "word in order"
else:
     print "word is not in order"