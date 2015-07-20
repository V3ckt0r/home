import os
import subprocess

path = os.getcwd()

print path
print "Print successful"

#changePath = os.chdir("/home/b/test_python_scripts/LearnPythonHardWay/test")
changePath = os.chdir("test/")

print os.getcwd()
print "Print successful"

subprocess.call("ls")












#This is user the subprocess libaray
"""
subprocess.call(["ls", "-lta"])
print "next...."
subprocess.call(["cd", "ex13"])
print "Done..."
subprocess.call(["ls", "-ltr"])
"""

