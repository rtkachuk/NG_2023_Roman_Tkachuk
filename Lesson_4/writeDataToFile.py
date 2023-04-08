def writeListToFile(pathToFile, rows):
    file = open(pathToFile, "a")
    for line in rows:
        file.write(line + "\n")
    file.close()

lst = [
    "Hello world",
    "Test",
    "123"
]

writeListToFile("test2.txt", lst)