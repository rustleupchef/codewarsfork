address = ''
allAddresses = ""
output = ""
while address != "END":    
    commaCount = 0
    address = input()
    for i in range(len(address)):
        if address[i] == "," and commaCount == 0:
            name = address[0:i]
            nameIndex = i
            commaCount += 1
        elif address[i] == "," and commaCount == 1:
            streetAdress = address[nameIndex:i]
            streetIndex = i
            commaCount += 1
        elif commaCount == 3:
            cityStatePostalCode = address[streetIndex:]
            output += name, "\n", streetAdress, "\n", cityStatePostalCode, "\n\n"
print(output)

