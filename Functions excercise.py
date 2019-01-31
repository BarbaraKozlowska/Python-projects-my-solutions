
#Define the function to print a blank line
def new_line():
    print()

#Define the function to print three blank lines
def three_lines():
    new_line()
    new_line()
    new_line()

#Define a function to print nine blank lines
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

#Define a function to print twenty five lines and clear the screen
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

#Print nine lines to console
print("Printing nine lines")
nine_lines()

#Print twenty five lines to console
print("Calling clear_screen()")
clear_screen()
