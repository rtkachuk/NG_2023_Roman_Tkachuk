def greetings(times=1):
    for counter in range(0, times):
        print ("Hello world!")

def showAripheticalOperation(a, b, operation):
    match(operation):
        case "+": print (summa(a,b))
        case default: print ("ERROR")

def summa(a, b):
    return a + b

greetings()
greetings(5)

showAripheticalOperation(2, 4, "-")