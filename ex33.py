shoplist = ['apple', 'banana', 'mango', 'jelly']
print len(shoplist)
print shoplist
shoplist.append('shoe')
print shoplist
del shoplist[0]
print shoplist
shoplist.sort()
print shoplist

shoplist.append(234)
print shoplist
shoplist.append(['brother','sister'])
print shoplist


zoo = 'monkey','lion','tiger'
print len(zoo)
print zoo
new_zoo = 'zebra', 'snake', zoo
print len(new_zoo)
print new_zoo

myitem = ()
print len(myitem)
print myitem
myitem = myitem, 2
print len(myitem)
print myitem
myitem = (2,)
print len(myitem)
print myitem