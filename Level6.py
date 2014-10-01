import zipfile
import StringIO
import re
z = zipfile.ZipFile("D:/python/channel.zip")
t = z.read("90052.txt")
for i in range (910):
	#print "hello"
	#print t
	m = re.search("nothing is \d+",t)
	if m:
		#print m.group(0)
		n=re.search("\d+",m.group(0))
		#print n.group(0)
		t = z.read(n.group(0)+".txt")
		print z.getinfo(n.group(0)+".txt").comment,