file = open("test2.txt", "r")

for line in file.readlines():
    print (line, end="")
file.close()