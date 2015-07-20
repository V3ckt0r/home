#!/urs/bin python

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here ating a cheese cake. what do you do?"
    print "1. take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    
    if bear =="1":
        print "The bear eats your face off. Good Job!"
    elif bear =="2":
	print "The bear eats your legs off. Good Job!"
    else:
	print "Well, doing %s is probably better. Bear runs away." %bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket Clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")

    if insanity == "1" or insanity =="2":
	print "Your body survues powered by a mind of jello. Good Job!"

    else:
	print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "you Stuble around and fall on a knife and die. Good job!"
