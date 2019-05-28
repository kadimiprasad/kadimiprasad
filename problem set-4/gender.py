class Person(object):
    def __init__(self):
        pass
    @staticmethod
    def getgender():
        return "unknown"

class Male:
    @staticmethod
    def getgender(self):
        return "male"

class Female:
    @staticmethod
    def getgender(self):
        return "female"

obj=Male( )
print("gender",obj.getgender())
obj1=Female( )
print("gender",obj1.getgender())