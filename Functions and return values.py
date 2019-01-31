
#Function to compare two numbers

def compare(a,b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


#Check given values
#Compare a < b
    
retvalue = compare(2, 5)
print(retvalue)

#Compare a > b
retvalue = compare(5, 2)
print(retvalue)

#Check if a == b

retvalue = compare(3, 3)
print(retvalue)

# Switch to user output
a = input ("Enter value for a: ")
b = input ("Enter value for b: ")

retvalue = compare(int(a), int(b))
print(retvalue)
