

def mix_up(a, b):
  # +++your code here+++
  a_list = list(a)
  b_list = list(b)
  size_a = len(a)
  size_b = len(b)
  new_a = ""
  new_b = ""
 # swap_a = b_list[0]+b_list[1]
 # swap_b = a_list[0]+a_list[1]

  while size_a > 0:
    if size_a <= 2:
      letter = b_list[size_a -1]
      size_a -= 1
      new_a = letter + new_a
      print new_a 
    else:
      letter =  a_list[size_a - 1]
      size_a -= 1
      new_a = letter + new_a
      print new_a


  while size_b > 0:
    if size_b <= 2:
      letter = a_list[size_a - 1]
      size_b -= 1
      new_b = letter + new_b
      print new_b
    else:
      letter = b_list[size_b -1]
      size_b -= 1
      new_b = letter + new_b
      print new_b
  
  return new_a + new_b

mix_up("test", "one")


"""
count = 0
word = "savage"
list_word = list(word)
first_letter = list_word[1]
result = ""

for letter in list_word:
   if letter == first_letter and count > 0:
     count += 1
     result += "*"
    # letter = "*"
   elif letter == first_letter and count == 0:
     print "Ignore"
     count += 1
     result += letter
   else:
     print "didn't work"
     print count
     print letter
     print first_letter
     count += 1
     result += letter


print result
"""
