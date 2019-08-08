fro = ['a','e','i','o','u']
input = ''
class Forbidden:
     def Method(self):
        global fro
        global input
        input = input("Enter the word")
        for var in fro:
             if var == input:
                 return True
             else:
                 return False
@staticmethod
def Function():
    obj = Forbidden
    print(obj.Method())
Forbidden.Function()







