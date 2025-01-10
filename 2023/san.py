# san.py 

def find_lowest(nums):
    low = -1
    for num in nums:
        if num < low:
            return num
        

'''
PROCEDURE findlow(nums){
    low ← -1
    FOR num IN nums {
        if (num < low) {
            RETURN num
        }
    }
}
'''
def find_lowest(nums):
    low = -100000
    for num in nums:
        if num > low:
            low = num
    return low
'''
PROCEDURE findlow(nums){
    low ← -100000
    FOR num IN nums {
        if (num > low) {
            low ← num
        }
    }
    RETURN low
}
'''
def find_lowest(nums):
    low = nums[0]
    for num in nums:
        if num < low:
            low = num    
        return low
'''
PROCEDURE findlow(nums){
    low ← nums[1]
    FOR num IN nums {
        if (num < low) {
            low ← num
        }
        RETURN low
    }
}
'''    
        
def find_lowest(nums):
    low = nums[0]
    for num in nums:
        if num < low:
            low = num    
    return low
'''
PROCEDURE findlow(nums){
    low ← nums[1]
    FOR num IN nums {
        if (num < low) {
            low ← num
        }
    }
    RETURN low
}
'''    

def find_lowest(nums):
    low = nums[0]
    for i in range(5):
        if nums[i] < low:
            low = nums[i]    
    return low
'''
PROCEDURE findlow(nums){
    low ← nums[1]
    i ← 1
    REPEAT 5 TIMES {
        if (nums[i] < low) {
            low ← num
        }
        i ← i +1
    }
    RETURN low
}
''' 
def find_lowest(nums):
    low = nums[0]
    i = 0
    while i < len(nums):
        if low > nums[i]:
            low = nums[i]
            i += 1
    return i
'''
PROCEDURE findlow(nums){
    low ← nums[1]
    i ← 1
    REPEAT UNTIL (i > LENGTH(nums)){
        if (nums[i] < low) {
            low ← num
            i ← i +1
        }
    }
    RETURN i
}
''' 

def find_lowest(nums):
    low = nums[0]
    i = 0
    while i < len(nums):
        if low > nums[i]:
            low = nums[i]
        i += 1
    return low

'''
PROCEDURE findlow(nums){
    low ← nums[1]
    i ← 1
    REPEAT UNTIL (i > LENGTH(nums)){
        if (low > nums[i]) {
            low ← nums[i]
        }
        i ← i +1
    }
    RETURN low
}
''' 

def find_lowest(nums):
    low = nums[0]
    i = 0
    while i < len(nums):
        if low > nums[i]:
            low = nums[i]
        i += 1
    return i

'''
PROCEDURE findlow(nums){
    low ← nums[1]
    i ← 1
    REPEAT UNTIL (i > LENGTH(nums)){
        if (low > nums[i]) {
            low ← nums[i]
        }
        i ← i +1
    }
    RETURN low
}
''' 