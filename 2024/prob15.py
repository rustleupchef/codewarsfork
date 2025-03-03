line = input()
line = line.split()
normalLine = ""
subscript = ""
for i in range(len(line[0])):
    if line[0][i].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        normalLine += line[0][i]
        subscript += " "
    else:
        subscript += line[0][i]
        normalLine += " "
print(normalLine)
print(subscript)