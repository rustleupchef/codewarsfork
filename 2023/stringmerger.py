

a = 'cat'
b = 'ate'

x = 'yzay'
y = 'axxb'

print("hey")    

def count_thing(a, b):
    temp = {}
    for i in range(len(a)):
        print(a[i], b[i])
        if (a.count(a[i]) + b.count(a[i]) )>(b.count(b[i]) + a.count(b[i])):
            if a[i] in temp.keys():
                temp[a[i]] += 1
            else:
                temp[a[i]] = 1
        else:
            if b[i] in temp.keys():
                temp[b[i]] += 1
            else:
                temp[b[i]] =1
        print(temp)
    
    print("unique: ", len(temp))
   

count_thing('yzay', 'axxb')      


