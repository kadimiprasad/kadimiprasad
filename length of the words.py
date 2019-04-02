file2 = input("Enter file name: ")

no_words = 0
with open(file2, 'r') as f:
    for line in f:
        w = line.split()
        no_words =no_words+ len(w)
print("Total words")
print(no_words)
