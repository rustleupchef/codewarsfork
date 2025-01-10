for data in (line.strip() for line in open(0)):
    if data == '0': break
    limit = len(data) - 4
    print(''.join(map(lambda x: 'x' if x[1].isdigit() and x[0] < limit else x[1], enumerate(data))))

def mask(str):
    masked = ""
    for letter in str[:-4]:
        if letter.isdigit():
            masked += "x"
        else:
            masked += letter
    return masked + str[-4:]
    
# 456-65-4859  --> xxx-xx-4859
while True:
    data = input()
    print(mask(data))
    # if data == '0':
    #     break
    # if len(data) == 19:
    #     print("xxxx-xxxx-xxxx-" + data[-4:])
    # else:
    #     print("xxx-xx-"+ data[-4:])