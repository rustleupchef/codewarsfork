
# Output sample
'''
7            +-----+ 
6            |     | 
5   /\       |     | 
4  +-+       |     | 
3  | | +-+   | ____|__    +---+ 
2 \| | | |   |/       \   |   | 
1  \ | | |   /         \  |   | 
0   +-------+           +-+---+ 
0123456789012345678901234567890
'''

#Sample Input
'''
30 8  
2 \| | | |   |/       \   |   | 
0   +-------+           +-+---+ 
1  \ | | |   /         \  |   | 
5   /\       |     | 
7            +-----+ 
3  | | +-+   | ____|__    +---+ 
4  +-+       |     | 
6            |     |
'''

#read in the garbled text file
path = '2019/2019data/prob11-3-in.txt'
handle = open(path) # open the file handle
full_text = handle.read()
# print(full_text)
lines = full_text.split('\n')

line_1 = lines[0]
width = line_1.split()[0]
num_lines = line_1.split()[1]

# print(width)
# print(num_lines)
pic_list = lines[1:]
for i in range(len(pic_list)):
    loc = pic_list[i].find(" ")
    ptup = (int(pic_list[i][:loc]), pic_list[i][loc:])
    # print(ptup)
    pic_list[i] = ptup
pic_list.sort()
for l in reversed(pic_list):
    s= str(l[0]) + l[1]
    print(s)
nums = '0123456789'
bottom = ''
index = 0
for i in range(int(width)+1):
    bottom += nums[index%10]
    index += 1
print(bottom)