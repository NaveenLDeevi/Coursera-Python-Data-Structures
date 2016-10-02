<<<<<<< HEAD
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
=======
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
>>>>>>> 5ab7a4630064b4d01744ed8749a76b710605b00d
print 'There were',counter,'lines in the file with From as the first word'