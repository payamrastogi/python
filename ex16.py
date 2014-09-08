from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "if you don't want that, hit CTRL-C (^C)."
print "Otherwise hit Enter"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye..."
target.truncate()

print "Now, I'm gonna ask you for three lines"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these lines to the file."

target.write(line1+"\n")
target.write(line2+"\n")
target.write(line3+"\n")


print "finally, we close it."
target.close()
