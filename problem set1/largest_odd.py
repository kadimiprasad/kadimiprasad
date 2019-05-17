
# kadimi.prasad
# to print the largest odd number in 10 numbers
#date:19-03-2019

k= input("enter the num:")
n1 = map(int,k.split())
list1= []
list2 = []
for i in n1:
    if i % 2 ==1:
        list1.append(i)
    else:
        list2.append(i)
if len(list2) == 10:
    print("no odd numbers")
elif len(list2) < 10:
    print (max(list1))
