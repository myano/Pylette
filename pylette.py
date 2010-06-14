# Pylette
# Version 0.1
#
# Written by: Nathan Chowning
#
# Visit http://github.com/nchowning/Pylette for more information

import sys
import getopt

# --help function
def usage():
	print "Quit being a faggot"

def main(argv):
	count = 0 # Number of colors to use
	try:
		opts, args = getopt.getopt(argv, "hc", ["help", "count="])

# Flag/argument error handling
	except getopt.GetoptError:
		print "You have specified an incorrect flag/value!"
		usage()
		sys.exit(2)

# Check for flags.  If flags aren't present, count remains at 0
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-c", "--count"):
			count = arg
	source = "".join(args)
	print count

if __name__ == "__main__":
	main(sys.argv[1:]) # removes sys.argv[0] (Script name) since that's garbage
