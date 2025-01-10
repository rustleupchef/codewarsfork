w = [2,5,7,9,10] #len 5

x = [-3, 1, 4]

y = []

z = [35]


def mergeArrays(arr1, arr2):
    arr3 = []
    i = 0
    j = 0
    # k = 0
 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            # k = k + 1
            i = i + 1
        else:
            arr3.append(arr2[j])
            # k = k + 1
            j = j + 1
 
    while i < len(arr1):
        arr3.append(arr1[i])
        # k = k + 1
        i = i + 1
 
    while j < len(arr2):
        arr3.append(arr2[j])
        # k = k + 1
        j = j + 1
        
    return arr3

def median(arr):
    if len(arr)%2 ==0:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2])/2
    else:
        return arr[len(arr)//2]
    

def merged_median(a,b):
    return median(mergeArrays(a,b))

print(merged_median(w,x)) # should be 4.5
print(merged_median(w,y)) # should be 7

print(merged_median(y,x)) # should be 1

print(merged_median(x,z)) # should be 2.5