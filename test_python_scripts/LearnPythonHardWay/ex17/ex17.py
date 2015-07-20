#!/usr/bin/env python
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print " Copying from %s TO %s" % (from_file, to_file)

# WE COULD DO THESE TWO ON ONE LINE, HOW?
in_file = open(from_file)
indata = in_file.read()
#in_file = open(from_file, 'r')

print "The input file is %d bytes long" % len(indata)

print " does the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alriht, all done."

out_file.close()
in_file.close()
