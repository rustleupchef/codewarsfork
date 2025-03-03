graph = []
values = []
letters = []
size = input().split()
count = 0
for i in range(int(size[1])+2):
    graph.append(input())

for row in range(len(graph)):
    for column in range(6, 6 + int(size[0])*2):
        #print(graph[row][column])
        #print(column)
        if graph[row][column] == "X":
            letterIndex = ((column-6)//3)
            if len(values) < letterIndex +1:
                values.append(1)
            else:
                values[letterIndex] += 1
        elif graph[row][column].lower() in "abcdefghijklmnopqrstuvwxyz":
            letters.append(graph[row][column])
for letter in letters:
    print(f"{letter}: {values[0]}")