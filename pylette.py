# Pylette
# Version 0.1
#
# Written by: Nathan Chowning
#
# Visit http://github.com/nchowning/Pylette for more information

import sys
import getopt

# This function checks for flags/arguments that have been passed via command line
# If no flags were passed, it assigns three arguments to rgb[]
def flarg(argv, rgb):
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

    # Ensures that count is 16 or less.
    if int(count) > 16:
        print "Pylette only supports Palettes with 256 colors.  You have specified a larger palette!"
        usage()
        sys.exit(2)

    if len(sys.argv) < 2:
        print "YOU ENTERED NOTHING!"

    # If count is still 0, arguments have been supplied.  Assign them.
    if len(sys.argv) > 1 and int(count) == 0:
        rgb[0] = sys.argv[1]
        rgb[1] = sys.argv[2]
        rgb[2] = sys.argv[3]

    return count

# --help function
def usage():
    print "Quit being a faggot"

def main():
    rgb = [0, 0, 0] # Creates the rgb array in the main function's scope

    count = flarg(sys.argv[1:], rgb)

if __name__ == "__main__":
    main()
