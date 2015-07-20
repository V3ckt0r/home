#!/usr/bin/env python

from sys import argv

script, first, second, third = argv

answer=raw_input("Is it hot or cold?:")

print "So you are %r" % answer
print "So you are " + answer

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third 
