# Format a string with %s
breed = "beagle"
print("Did you see a %s?" % breed)

# Format an integer with %d
dogs = 42
print("There are %d dogs." % dogs)

# Format a float with %f
grade = 87.385
print("Your current grade is %f!" % grade)

# Format a float with %.[precision]f
grade = 87.385
print("Your current grade is %0.1f!" % grade)

# Format multiple values
dogs = 42
cats = 18
exclamation = "Wow!"
print("There are %d dogs and %d cats. %s!!!!" % (dogs, cats, exclamation))

# Format right aligned with %[minWidth]
dogs = 42
cats = 30
print("%10s %10s" % ("dogs", "cats"))
print("%10d %10d" % (dogs, cats))

# Format left aligned with %[minWidth]
dogs = 42
cats = 3
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))