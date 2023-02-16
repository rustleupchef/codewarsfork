
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
# save the text in the .txt file as a long multiline string
full_text = handle.read()
# print(full_text)

# convert the string into a list (1 line per element)
lines = full_text.split('\n')

# Extract the 1st element (meta data)
line_1 = lines[0]
# From the first line get the number of lines and height
width = line_1.split()[0]
num_lines = line_1.split()[1]

# print(width)
# print(num_lines)
# create a list that excludes the meta data element
pic_list = lines[1:]

# iterate through the pic_list and separate the line numbers from the pic
# in a tuple
for i in range(len(pic_list)):
    loc = pic_list[i].find(" ")
    ptup = (int(pic_list[i][:loc]), pic_list[i][loc:])
    # print(ptup)
    pic_list[i] = ptup

# sort the list so that the line numbers are in order
pic_list.sort()

# Iterate through the reversed sorted list and print each line
# as you print reformat them into a string not tuple
for l in reversed(pic_list):
    s= str(l[0]) + l[1]
    print(s)
    
# print the column numbers
nums = '0123456789'
bottom = ''
index = 0
for i in range(int(width)+1):
    bottom += nums[index%10]
    index += 1
print(bottom)