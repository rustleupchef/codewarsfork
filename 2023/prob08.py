

# given 2 integers, the 1st is the base
# the 2nd is the exp

# figure out what the power was....

base = int(input())
power = int(input())

new_pow = 1* base
count = 1
while power > new_pow:
    new_pow*= base
    count += 1
print(base, "^" ,count,"=",power)
