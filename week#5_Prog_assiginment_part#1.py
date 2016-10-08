name= raw_input('Enter the name:')
file = open(name)
counts = dict()
for i in file:
	i = i.rstrip()
	if i.startswith('From:'):
		x=(i.split())[1]
		counts[x]=counts.get(x,0)+1
bigcount = None
bigword = None

for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigcount = count
		bigword = word
print bigword,bigcount