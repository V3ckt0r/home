#!/usr/bin python

import sys
from sys import argv
import subprocess
import os

script, count = argv
dirname = "ex" + count
scriptname = dirname + ".py"


print "Creating new directory for %s" %count

subprocess.call(["mkdir",  dirname])
#subprocess.call(["mkdir", '"ex" + count'])

print "Created dir"

os.chdir(dirname)
subprocess.call(["touch", scriptname])
f = open(scriptname, 'w')
sys.stdout = f
print '#!/usr/bin python'

f.close()

#subprocess.call(["echo", '#!/usr/bin python', '>', scriptname])

subprocess.call(["ls", "-lta"])
subprocess.call(["echo", "script complete..."])
#print "script complete"



