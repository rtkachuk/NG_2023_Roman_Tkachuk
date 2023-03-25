# Lists are: Changeable, ordered, allow duplicates []

items = [ "mouse", "keyboard", True, 42, -512, "HELP" ]

# Add items to list

items.append("CPU")
print(items)

# Insert to list

items.insert(2, "RAM")
print(items)

# Edit first element

items[0] = 15
print (items)

# Show elements on the screen

print ("=====================")
print (items) # Show as is
print (items[1]) # Show only first
print (items[:3]) # Show elements from first to third
print (items[4:]) # Show elements from fourth to last
print (items[-1]) # Show last element
print (items[1:3]) # Show from first to third

# Determine: if element present in the list

print ("=====================")
if "RAM" in items:
    print ("YES")
else:
    print ("NO")
print ("=====================")

# List all elements one by one

for element in items:
    print (element)

print ("=====================")

# Sort items

numbs = [ 6, 10, 5, 8, 4, 2, 7, 1, 9, 3 ]
numbs.sort()
print (numbs)

# Copy lists

print ("=====================")
numbsCopy = numbs.copy()
numbsCopy[0] = "DANGER"
print (numbs)

# Join lists

print ("=====================")
items.extend(numbsCopy)
print (items)

# Get list length
print ("=====================")
print (len(items))

# Remove element from list

print ("=====================")
items.remove("DANGER")
print (items)