fname = input("Enter file name: ")
lines = 0
with open(fname, 'r') as f:
    for line in f:
        lines =lines + 1
print("Number of lines:")
print(lines)
