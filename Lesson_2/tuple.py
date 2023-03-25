# Tuples are: Ordered, allow duplicates, UNCHANGEABLE ()

items = ( "first", 2, True)
print (items)

# Access to elements are the same as in lists

# HACK TO MAKE IT CHANGEABLE!!!!

buffer = list(items)
buffer.append("OMG")
items = tuple(buffer)
print (items)

# PACK/UNPACK TUPLE!!!!

wow = (6, "HELP", True, 12)
(first, second, third, fourth) = wow
print (second)

# Loop through tuple

print ("=====================")
i = 0
while i < len(wow):
    print (wow[i])
    i = i + 1

# Join tuples

print ("=====================")

result = items + wow
print (result*2)