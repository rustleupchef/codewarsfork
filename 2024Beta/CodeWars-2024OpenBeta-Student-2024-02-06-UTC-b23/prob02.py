nums = input()      # "3 7 19"
nums = nums.split() # ['3', '7', '19']

h, w, limit = int(nums[0]), int(nums[1]),int(nums[2])

p = (h + w)*2
a = h * w
if a < limit:
    print(p, a, "NEED MORE SPACE")
else:
    print(p, a, "ENOUGH SPACE")