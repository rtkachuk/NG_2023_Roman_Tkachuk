try:
    f = open("test1.txt", "x")
except FileExistsError:
    print("Such file already exists!")
    print("Opening file for append")
    f = open("test1.txt", "a")
finally:
    lst = [ "test1", "test2", "test3" ]
    for line in lst:
        f.write(line + "\n")
    f.close()