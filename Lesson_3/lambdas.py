lst = [ 2, 4, 6, 8, 10]
print (list(map(lambda element: element + 1, lst)))

lst2 = [2, 3, 4, 5, 6, 7]
print (list(map(pow, lst, lst2)))

lst3 = []
for element in lst:
    lst3.append(element+1)
print (lst3)

ad = lambda x: x + 1
print (ad(2))

# Lomaet mozg

def multpl(n):
    return lambda a: a * n

myMultipl = multpl(2)
print (myMultipl(11))