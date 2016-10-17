handle = open('mbox-short.txt')
number = dict()
for i in handle:
	if i.startswith('From'):
		x = i.split()
		if len(x)>3:
			y = x[5]
			y = y.split(':')
			time = y[0]
			number[time]=number.get(time,0)+1
		else:
			continue
for (key,value) in sorted(number.items()):
	print key,value