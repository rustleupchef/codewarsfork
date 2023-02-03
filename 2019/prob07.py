import math
import time
# prob 07 

# M = 0 --> even
# M = 1 --> prime
# M = 2 --> perfect square
# M = 3 --> perfect cube (power of 3)


def is_even(num):
    return num % 2 == 0

def is_square(num):
    x = math.sqrt(num)
    if x % 1 == 0:
        return True
    else:
        return False
    
def is_cube(num):
    x = round(num**(1/3))
    # print(x, "^3", x**3, "=?", num)
    # time.sleep(1)
    if x ** 3 == num:
        return True
    else:
        return False
    
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def output(num, m):
    if m == 0:
        # use is even
        num += 1
        while is_even(num)==False:
            num += 1
        return num
    elif m == 1:
        # use is prime        
        num += 1
        while is_prime(num)==False:
            num += 1
        return num
    elif m == 2:
        # use is_square(num)
        num += 1
        while is_square(num)==False:
            num += 1
        return num
    elif m == 3:
        # use is_cube(num)
        num += 1
        while is_cube(num)==False:
            num += 1
        return num
    
while True:
    line = input()
    line = line.split()   
    n = int(line[0])
    m = int(line[1])
    if n == 0 and m == 0:
        break
    else:
        print(output(n,m))
    
    
# 999,999 1,000,000