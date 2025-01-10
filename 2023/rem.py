def remove_vowel_words(words):
	no_vowels = []
	for word in words:
		if len(word)>0 and word[0].lower() in 'aeiou':
			continue
		else:
			no_vowels.append(word)
	return no_vowels


words = ["James", "edna", "Thomas", "Hot Dog", "hippo", "Arthur", "", "Olivia"]

print('Expected: ["James", "Thomas", "Hot Dog", "hippo", ""]')
print('Actual:', remove_vowel_words(words))


'''
A 2018 survey of South African households found that only 10.4% of households have Internet access and 21.5% have a computer.
Which of these would be the least effective way to reduce the digital divide across households?
Choose 1 answer:
Choose 1 answer:
(Choice A)   Providing free subscriptions to an online video course about digital literacy
A
Providing free subscriptions to an online video course about digital literacy
(Choice B)   Setting up Internet infrastructure in highly populated areas
B
Setting up Internet infrastructure in highly populated areas
(Choice C)   Donating refurbished laptops to low-income families
C
Donating refurbished laptops to low-income families
(Choice D)   Partnering with an Internet Service Provider to offer discounted rates for Internet access
D
Partnering with an Internet Service Provider to offer discounted rates for Internet access



Which of these statements about the digital divide is true?
Choose 1 answer:
Choose 1 answer:
(Choice A)   Governments can never restrict Internet access for their citizens, thanks to the redundancy in Internet routing.
A
Governments can never restrict Internet access for their citizens, thanks to the redundancy in Internet routing.
(Choice B, Checked)   The digital divide is affected by geography; some areas are harder to connect to the Internet than others.
B
The digital divide is affected by geography; some areas are harder to connect to the Internet than others.
(Choice C)   Only government actions can help bridge the digital divide.
C
Only government actions can help bridge the digital divide.
(Choice D)   If everyone in the world had a computer and access to the Internet, there would be no more digital divide.
D
If everyone in the world had a computer and access to the Internet, there would be no more digital divide.


In 2015, researcher Teresa Correa studied social media use in a sample of 18 to 29 year olds in Chile. She was interested in this age group as they are often called "digital natives," the youth that grew up around computers and the Internet, and she wanted to understand the differences in digital skills amongst them.
Which of the following research findings describe a digital divide?
👁️Note that there are 2 answers to this question.
Choose 2 answers:
Choose 2 answers:
(Choice A)   There was not a significant difference in digital skills levels between the age groups 18-24 and 25-29.
A
There was not a significant difference in digital skills levels between the age groups 18-24 and 25-29.
(Choice B)   There was no correlation between digital skill levels and frequency of using Facebook.
B
There was no correlation between digital skill levels and frequency of using Facebook.
(Choice C)   There was a positive correlation between education levels and digital skills.
C
There was a positive correlation between education levels and digital skills.
(Choice D)   There was a significant difference between the level of digital skills between the men and women in the sample.
D
There was a significant difference between the level of digital skills between the men and women in the sample.

'''
