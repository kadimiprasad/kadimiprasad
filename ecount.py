class Ecount:
    def __init__(self):
        print("count")
    def eCount(self):
            with open("sample.txt", "r+") as fobj:
                for line in fobj:
                    word = line.split()
                    print word
                    for i in word:
                        for letter in i:
                            print letter
                            if letter == 'e':
                                return True
fobj = Ecount()
value = fobj.eCount()
print value
if value == True:
    print "The file contains the e letter"
else:
    print "The letter does not contains the e letter"
