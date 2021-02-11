n = input()
hms = n.split(" ")
for i in range(3):
    hms[i] = int(hms[i])
print(hms)



if(hms[0] >= hms[1]/hms[2]):
    print(n + ". I will make it." )
else:
    print(n + ". I will be late.")