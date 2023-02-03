spellings = {
    '0':"ZERO",
    '1':"ONE",
    '2':"TWO",
    '3':"THREE",
    '4':"FOUR",
    '5':"FIVE",
    '6':"SIX",
    '7':"SEVEN",
    '8':"EIGHT",
    '9':"NINE",
    '10':"TEN",
    '11':"ELEVEN",
    '12':"TWELVE",
}

line = input()
# split the numbers entered into s list
nums = line.split()
# remove the 999
nums.pop()

#create a dictionary to hold {letter: quantity_needed, }
needed = {}
# loop through the nums entered
for num in nums:
    # convert the number into its spelling
    word = spellings[num]
    # loop through that spelling one letter at a time
    for letter in word:
        # if the letter is in the dictionary only 
        # update if you need more letters
        if letter in needed.keys():
            if needed[letter] < word.count(letter):
                needed[letter] = word.count(letter)
        # if the letter is not saved yet add it to the dictionary
        else:
            needed[letter] = word.count(letter)
            
            
# build the srting to be printed
# move them into a list to sort
out = ""
lets = []

for k in needed.keys():
    for i in range(needed[k]):
        lets.append(str(k))
        
lets.sort()
# print(nums)
# print(lets)
for num in nums:
    out+= num + " "

# take off the last space char and add a period as specified
out = out[:-1] +"."

#Next add the letters to the out string in alpha 
# separated by spaces
for l in lets:
    out += " " + l

print(out)


         
