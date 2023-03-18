# Example of the python ariphmetics
#

#value1 = 1
#value2 = 5
#print (value1 + value2)

# int - integer numbers
# float - float numbers
# str - string

print ("Enter current year: ")
currentYear = int(input()) # use str to transform number to text
userAge = int(input ("Enter your age: "))
lastYear = int(input("Enter desired year: "))

ageAccordingYear = userAge + (lastYear - currentYear)

print ("In {} your age will be: {}".format(lastYear, ageAccordingYear))