from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d byte long" %len(in_data)

print "Does the output file exists? %r" %exists(to_file)

print "Ready, hit to Return to continue, CTRL-C to abort."
raw_input("?")

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, done."

out_file.close()
in_file.close()