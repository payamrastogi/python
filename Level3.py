import re
#file_object = open("/media/payam/Application/python/Level2.txt", 'r')
word = ""
for line in open("/media/payam/Application/python/Level3.txt", 'r'):
	m = re.search("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]",line)
	if m:
		print m.group(0)
		n=re.search("[a-z]",m.group(0))
		print n.group(0)
