print("program opened")

# The input and output location
InputFile = open ('unsorted_fruits.txt', 'r')
OutputFile = open('sorted_fruits.txt', 'w')

# Reading the input file
Fruits = InputFile.readlines()

# Sorting the items in the list
Fruits.sort()

# removing the blank lines and writing the file
for fruit in Fruits:
    if fruit != "\n": # if there is blank space, skip it
        OutputFile.write(fruit) # otherwise, write the fruit in the output list

# Close the input and output file
InputFile.close()
OutputFile.close()


print("program completed")
                  

