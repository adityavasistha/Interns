import re
i = raw_input("enter the string ")
y = re.findall("[A-Z]+?", i)
print "length=" , len(y)