import re
#file_object = open("/media/payam/Application/python/Level2.txt", 'r')
word = ""
for line in open("/media/payam/Application/python/Level2.txt", 'r'):
	m = re.search("[a-z]",line)
	if m:
		word = word+m.group(0)
print word


#http://www.pythonchallenge.com/pc/def/equality.html
