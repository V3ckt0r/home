#!/usr/bin/env python

import subprocess
import os

print "This is a test"

#subprocess.call(["source", "/home/b/test_python_scripts/sourceThis.sh"])

#subprocess.call(["echo", "TEST_VAR"])

#execfile("/home/b/test_python_scripts/sourceThis.sh")

print os.environ['HOME']

print os.environ.get('ORACLE_HOME')


"""
subprocess.Popen(('env'), stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', '$PATH'), stdin=ps.stdout)
ps.wait()

subprocess.call(["echo","$TEST_VAR"])
subprocess.call(["echo", "$PATH"])
subprocess.call(["env | grep $PATH"])
"""

print "Fin"
