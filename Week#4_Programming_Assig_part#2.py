fname = raw_input('Enter file name:')
f = open(fname)
counter = 0
for lines in f:
	lines = lines.rstrip()
	if lines.startswith('From:'):
		x = lines.split()
		print x[1]
		counter = counter + 1
	else:
		continue
print 'There were',counter,'lines in the file with From as the first word'