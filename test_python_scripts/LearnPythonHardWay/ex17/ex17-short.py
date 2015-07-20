#!/usr/bin/env python
from sys import argv
import shutil


script, from_file, to_file = argv

shutil.copy(from_file, to_file)



print "done..."	

