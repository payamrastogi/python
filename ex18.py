def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
def print_one(args):
	print "arg1: %r" %args
	
def print_none():
	print "I have nothing to print"
	
print_two("Payam", "Rastogi")
print_two_again("Payam", "Rastogi")
print_one("Payam")
print_none()