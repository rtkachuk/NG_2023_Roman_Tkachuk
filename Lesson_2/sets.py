# Sets are: UNORDERED, UNCHANGEABLE, UNINDEXED {}

items = { "apple", "microsoft", "linux", "apple" }
print (items)

# Get data
print ("=====================")
for element in items:
    print (element)

# Check if item inside set
print ("=====================")
print ("linux" in items)

# Add items to set
print ("=====================")
items.add("linux")
items.add("FreeBSD")
print (items)

# Join sets
print ("=====================")
first = { "linux", 15, True, 24 }
second = { 15, False, "linux", "unix" }
first.update(second)
print (first)

# Remove objects
print ("=====================")
first.remove(15)
first.discard(15)
first.discard(15)
first.discard(15)
first.discard(15)
first.discard(15)
first.discard(15)
print (first)

# Loop over set

print ("=====================")
for element in first:
    print (element)