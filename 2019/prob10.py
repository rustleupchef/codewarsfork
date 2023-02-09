done = False
inputs = []
while (not done):
    inp = input("Input data or input D to be done")
    if(inp == 'D'):
        done = True
    else:
        inputs.append(inp)

for x in range(len(inputs)):
    if inputs[x].find(":") != -1:
        year = int((inputs[x][0:4]))
        month = int((inputs[x][5:7]))
        day = int((inputs[x][8:10]))
        age = int((inputs[x][11:len(inputs[x])]))
        if(month == 2 and day == 29):
            day = 28
            if((year + age) % 4 == 0 and not ((year+age) % 100)):
                day = 29
            if((year + age) % 400 == 0):
                day = 29
        if (age > 0):
            year = year + age
            month = str(month)
            if(len(month) == 1):
                month = "0" + month
            day = str(day)
            if(len(day) == 1):
                day = "0" + day
            print("Will be " + str(age) + " on " + str(year) + "-" + month + "-" + day + " if born on " + inputs[x][0:10])
        if (age == 0):
            month = str(month)
            if(len(month) == 1):
                month = "0" + month
            day = str(day)
            if(len(day) == 1):
                day = "0" + day
            print("Will still be 0 up to " + str(year+1) + "-" + str(month) + "-" + str(day) + " if born on " + inputs[x][0:10])
            
    else:
        year1 = int((inputs[x][0:4]))
        month1 = int((inputs[x][5:7]))
        day1 = int((inputs[x][8:10]))
        year2 = int((inputs[x][11:15]))
        month2 = int((inputs[x][16:18]))
        day2 = int((inputs[x][19:21]))
        if(month1 == 2 and day1 == 29):
            day1 = 28
        if(month2 == 2 and day2 == 29):
            day2 = 28
        if(month2 > month1):
            year2 = year2 + 1
        if(month2 == month1):
            if(day2 >= day1):
                year2 = year2 + 1
        age = year2 - year1 - 1
        gj = ""
        if (age > 99):
            gj = " (good job!)"
        print("If born on " + inputs[x][0:10] + ", will be " + str(age)+ " years old on " + inputs[x][11:21] + gj)