#Coursera-DataStructures programming assiginment 2
# Write a program that prompts for a file name, then opens that file and reads through the file, 
#looking for lines of the form:X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute 
#the average of those values and produce an output as shown below. Do not use the sum() 
#function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
#you are testing below enter mbox-short.txt as the file name.
#

#Start of program#
input = raw_input('Enter the name of the file:')
input = open(input,'r')
number = 0
total = 0
for i in input:
	if not i.startswith('X-DSPAM-Confidence:'):
		continue
	i = i.strip()
	x = i[(len(i)-7):len(i)]
	x = float(x)
	number = number + 1
	total = total + x
Average = total/number
print "Average Spam confidence:",Average
