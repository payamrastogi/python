import urllib2
import urllib
import re
data = {}
req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579')
response = urllib2.urlopen(req)
the_page = response.read()
for i in range (0,400):
	m = re.search("the next nothing is \d+",the_page)
	if m:
		print m.group(0)
		n=re.search("\d+",m.group(0))
	values= {'nothing' : n.group(0)}
	data = urllib.urlencode(values)
	print data
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
	full_url = url +'?'+data
	req = urllib2.Request(full_url)
	response = urllib2.urlopen(req)
	the_page = response.read()
#http://www.pythonchallenge.com/pc/def/peak.html
