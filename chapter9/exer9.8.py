# I was driving on the highway the other day and I happened to notice my odometer.
# Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
# miles, for example, I’d see 3-0-0-0-0-0.
# Now, what I saw that day was very interesting. I noticed that the last 4 digits were
#
# palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
#
# palindrome, so my odometer could have read 3-1-5-4-4-5.
#
# “One mile later, the last 5 numbers were palindromic. For example, it could have read
#
# 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
#
# you ready for this? One mile later, all 6 were palindromic!
#
# “The question is, what was on the odometer when I first looked?”
#
#
# Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
#
# these requirements.


# cat talk 2
#
 def odometer_reading ():
	for reading in range(100000, 999996):
		if str(reading)[2:] == str(reading)[:1:-1]:
			reading += 1
			if str(reading)[1:] == str(reading)[5:0:-1]:
				reading += 1
				if str(reading)[1:-1] == str(reading)[-2:0:-1]:
					reading += 1
					if str(reading) == str(reading)[::-1]:
						print('All palindrome: ', reading - 3)

odometer_reading()

[Solution link] (http: // thinkpython2. com/ code/ cartalk2. py)

# Output

All palindrome:  198888

All palindrome:  199999

