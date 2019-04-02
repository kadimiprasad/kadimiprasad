name = input("Enter file name: ")
word = input("Enter word")
c= 0
with open(name, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if i == word:
                c=c + 1
print("Occurrences of the word:")
print(c)
