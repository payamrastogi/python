import re
word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
L = list(word)
for i in range(len(L)):
	if re.match("\w",L[i]):
		if L[i]=='y':
			L[i] = 'a'
		elif L[i] == 'z':
			L[i] = 'b'
		else:
			L[i] = chr(ord(L[i])+2)
word = ''.join(L)
print word

http://www.pythonchallenge.com/pc/def/ocr.html