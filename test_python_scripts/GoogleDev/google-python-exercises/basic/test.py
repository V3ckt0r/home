
def remove_adjacent(nums):
  list1 = []
  for num in nums:
    if num not in list1 == True:
      list1.append(num)
  
  print list1
  return list1

remove_adjacent([1,2,2,3,4,5,5])

def front_x(words):
  # +++your code here+++
  list1 =[]
  list2 = []
  for word in words:
    if word[0] == "x":
      list1.append(word)
      print list1
    else:
      list2.append(word)
      print list2

   # if not "x" in word:
   #   list1 += word

  return list1 + list2

#front_x(["this","xisd","az","xdf"])


def match_ends(words):
  # +++your code here+++
  string_count = 0
  for word in words:
    if len(list(word)) >= 2:
      if word[0] == word[len(word)-1]:
        string_count += len(word)
  print string_count
  print words
  return string_count

#match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
#print "expected 3"
#match_ends(['', 'x', 'xy', 'xyx', 'xx'])
#print "excpected 2"
#match_ends(['aaa', 'be', 'abc', 'hello'])
#print "expected 1"



def not_bad(s):
  # +++your code here+++
  n = s.find('not')
  b = s.find('bad')
  if n != -1 and b != -1 and b > n:
    s = s[:n] + 'good' + s[b+3:]
    print s
  return s

#not_bad('This dinner is not that bad')

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

#front_back("abcde", "xyz")
