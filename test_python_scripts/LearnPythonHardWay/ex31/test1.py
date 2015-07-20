#!/usr/bin python
import os
import sys
from sys import argv
import subprocess

text_file = "loshtobo.txt"

print "What option do you want to do?"
print "Option 1: will make loshtobo"
print "Option 2: will make boshiro"
print "Option 3: will make topko"

option = raw_input("> ")

if option == "1":
    print "loshtobo!"
    #if os.chdir("loshtobo") == 1:
    if os.path.exists("loshtobo/"):
        if os.path.isfile("loshtobo/"+text_file):
            print "File already exists"
        else:
            print "File doesn't exists, creating file"
            subprocess.call(["touch", text_file])
	    print "File created....stream1 complete"
    else:
        print "Dir doesn't exist, creating it."
	subprocess.call(["mkdir", "loshtobo"])
	os.chdir("loshtobo")
	subprocess.call(["touch", text_file])
	f =open(text_file, 'w')
	f.write("This is some loshtobo text...\n")
	#Don't do it this way!
	#sys.stdout = f
	#print "This is some loshtobo text..."
	f.close()
	print "File created successfully"

elif option == "2":
    print "boshirooooo!"
    
else:
    print "ale....ale gumbale"        
