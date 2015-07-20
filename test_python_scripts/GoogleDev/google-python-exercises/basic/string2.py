#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  word = len(s)
  if word >= 3:
    ending = s[word-3:]
    if ending == 'ing':
     # s = s[:word-3] + 'ly'
      s = s + 'ly'
      return s
    else:
      return s + 'ing'
  
  
  return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  n = s.find('not')
  b = s.find('bad')
  if n != -1 and b != -1 and b > n:
    s = s[:n] + 'good' + s[b+3:]
  return s

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  import math
  a_count = len(a)
  b_count = len(b)

  if (a_count % 2 == 0) and (b_count % 2 == 0):
    a_half = a_count / 2
    b_half = b_count / 2
    a_front = a[:a_half]
    a_back = a[a_half:]
    b_front = b[:b_half]
    b_back = b[b_half:]
   # print a_front + b_front + a_back + b_back
    return a_front + b_front + a_back + b_back
  elif ((a_count % 2 != 0) and (b_count %2 != 0)) or ((a_count % 2 ==0) and (b_count %2 !=0)):
    a_half = int(float(math.ceil(a_count /2.0)))
    b_half = int(float(math.ceil(b_count /2.0)))
    a_front = a[:a_half]
    a_back = a[a_half:]
    b_front = b[:b_half]
    b_back = b[b_half:]
   # print a_front + b_front + a_back + b_back
    return a_front + b_front + a_back + b_back
  else:
   # print "Jack shit"
    return "null"

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()