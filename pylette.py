#!/usr/bin/python
# Pylette
# Version 0.1
#
# Written by: Nathan Chowning
#
# Visit http://github.com/nchowning/Pylette for more information

import sys, getopt

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
    print "****************"
    print "* Pylette Help *"
    print "****************\n"
    print "To generate 16 shades of a single color:"
    print "\tpylette.py RRR GGG BBB\n"
    print "To generate 16 shades of multiple colors:"
    print "\tpylette.py --count 16\n"

# Shade creation function.  This function takes the shade given to it (in RRR GGG BBB format) and
# generates 15 additional shades based on how light/dark the given color is
def shades(rgb):
    valmin = 0 # General minimum value
    valmax = 255 # General maximum value

    # Generate an average of the RGB values (to determine, generally, how light/dark the shade is)
    divav = (int(rgb[0]) + int(rgb[1]) + int(rgb[2])) / 3

    # This part is dumb and I need to come up with a better way of doing this.
    # My equations require arrays of a predetermined size (since this was written in c++ originally)
    redar = [0] * 16
    greenar = [0] * 16
    bluear = [0] * 16

    starter = 14 - (((valmax - divav) / 16) - 1) # Used to determine starting shade number

    # This section assigns the original color to the starting shade array
    redar[starter] = rgb[0]
    greenar[starter] = rgb[1]
    bluear[starter] = rgb[2]

    down = (divav / 16) - 1 # Loop control variable for the following loop

    # Loop that subtracts 16 from an RGB value (as long as the current value is greater than or equal
    # to 16) and assigns it to the next position in the shade array
    while (int(down) >= 0):
        if int(redar[down + 1]) >= 16:
            redar[down] = int(redar[down + 1]) - 16
        else:
            redar[down] = 0

        if int(greenar[down + 1]) >= 16:
            greenar[down] = int(greenar[down + 1]) - 16
        else:
            greenar[down] = 0

        if int(bluear[down + 1]) >= 16:
            bluear[down] = int(bluear[down + 1]) - 16
        else:
            bluear[down] = 0

        down = int(down) - 1 # Increment LCV

    controller = starter # Loop control variable for the following loop

    # Loop that adds 16 from an RGB value (as long as the current value is less than or equal
    # to 236) and assigns it to the next position in the shade array
    while (int(controller) + 1 <= 15):
        if int(redar[controller]) <= 239:
            redar[controller + 1] = int(redar[controller]) + 16
        else:
            redar[controller + 1] = 255

        if int(greenar[controller]) <= 239:
            greenar[controller + 1] = int(greenar[controller]) + 16
        else:
            greenar[controller + 1] = 255

        if int(bluear[controller]) <= 239:
            bluear[controller + 1] = int(bluear[controller]) + 16
        else:
            bluear[controller + 1] = 255

        controller = int(controller) + 1 # Increment LCV

    counter = 0 # Loop control variable for the following loop

    # Prints all 16 color shades from the shade array and ensures that they all have leading
    # zeros if their length is less than 3
    while (counter < 16):
        print str(redar[counter]).zfill(3), str(greenar[counter]).zfill(3), str(bluear[counter]).zfill(3)
        counter = counter + 1 # Increment LCV


def main():
    rgb = [0, 0, 0] # Creates the rgb array in the main function's scope

    count = flarg(sys.argv[1:], rgb) # Assigns a value to count from the flarg function

    # If no value was assigned to count (via the --count flag), this statement executes the
    # shades function (which uses rgb values passed on run-time
    if int(count) == 0:
        shades(rgb)

if __name__ == "__main__":
    main()
