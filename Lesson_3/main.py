#
# Dictionary: price, name, year, owner
#

def setOwner(dct, name):
    dct["name"] = name
    return dct

def initObject():
    item = {
        "price" : 0,
        "name" : "NONAME",
        "year" : 1975,
        "owner" : "NOOWNER"
    }

    return item

lst = [ setOwner(initObject(), "Andre"), 
       setOwner(initObject(), "Mike"), 
       setOwner(initObject(), "Anna") ]
print (lst)
