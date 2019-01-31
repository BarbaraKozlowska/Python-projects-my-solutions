# Compare function that returns 1 if a > b , 0 if a == b , and -1 if a < b

def comparison (a, b):
    if a > b:
        return 1 #prints 1 if a is greater than b
    elif a == b:
        return 0 #prints 0 if a is equal b
    elif a < b:
        return -1 #prints -1 if a is smaller than b

# Comparasion of the values from the assignment
print('From the addignment a > b where a = 5 and b = 2:', comparison(5, 2))
print('From the assignment a < b where a = 2 and b = 5:', comparison(2, 5))
print('From the assignment a = b where a = 3 and b = 3:', comparison(3, 3))

# Switch to user output
a = input ("Enter value for a: ")
b = input ("Enter value for b: ")


print(comparison (int(a), int(b)))
