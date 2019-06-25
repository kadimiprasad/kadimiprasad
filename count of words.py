# string=raw_input("enter")
# word = input("Enter word")
# c= 0
# for line in string:
#         # words = line.split()
#         for i in words:
#             if i == word:
#                 c=c + 1
# print("Occurrences of the word:")
# print(c)
#
#
#


    # str=raw_input("enter")
    # rstr1 = ''
    # index = len(str1)
    # while index > 0:
    #     rstr1 += str1[ index - 1 ]
    #     index = index - 1
    # print(rstr1)
    #
    #
    #
str=raw_input("enter")
List = list(str)
# print (List)
Uniq = set(List)
# print (Uniq)

for key in Uniq:
    print (key, str.count(key))