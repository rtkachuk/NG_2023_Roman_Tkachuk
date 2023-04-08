file = open("test1.txt", "w")

# x - create file (error if file exists)
# w - write to file (overwrite)
# a - append to file
# r - read file

file.write("Hello world")

# Close file
file.close()