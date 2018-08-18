my_name = "Sean Newman"
my_age = 56
my_height = 70 * 2.54 #centimeters
my_weight = 200 * 0.453592 #kilograms
my_eyes = "Brown"
my_teeth = "white"
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's pretty heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " % (my_age, my_height, my_weight, my_age + my_height + my_weight)