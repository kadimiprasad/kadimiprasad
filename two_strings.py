p = input("enter the string1")
p1 = input("enter the string2")
def two_string():
    if (p in p1) or (p1 in p):
        print("True")
    else:
        print("False")
two_string()