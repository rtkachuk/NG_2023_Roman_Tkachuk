# Dictionary helps us keep big structure of data

stats = {
    "CPU": "Ryzen 3600X",
    "RAM": {
        "Manufacturer": "Kingston",
        "Size": "16GB"
    },
    "HardDriveSpace": "4TB"
}

print (stats)
print (stats["CPU"])
print (stats["RAM"]["Size"])
stats["WIFI"] = "enable"
del stats["CPU"]
print (stats.keys())

print ("=====================")
# Loops keys

for key in stats.keys():
    print (key)

print ("=====================")
# Loop values

for value in stats.values():
    print (value)

print ("=====================")
# Loop over internal dict keys

for key in stats["RAM"].keys():
    print (key)