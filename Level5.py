import pickle
file_object = open("D:/python/Level5.txt", 'r')
file_write = open("D:/python/Level5.3.txt", 'w')
list_object = pickle.load(file_object)
for list2 in list_object:
	for (x,y) in list2:
		for i in range(y):
			file_write.write(x)
	file_write.write("\n")
file_write.close()