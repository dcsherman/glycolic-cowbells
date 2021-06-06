# converts temperature to fahrenheit or celsius

def print_options():
    print "Options:"
    print " 'p' print options"
    print " 'c' convert from celsius"
    print " 'f' convert from fahrenheit"
    print " 'q' quit the program"

def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0

choice = "p"
while choice != "q":
    if choice == "c":
        temp = input("Celsius temperature: ")
        print "Fahrenheit:", celsius_to_fahrenheit(temp)
    elif choice == "f":
        temp = input("Fahrenheit temperature: ")
        print "Celsius:", fahrenheit_to_celsius(temp)
    elif choice != "q":
        print_options()
    choice = raw_input("option: ")
	
# v2.7.10 throws FileError
# File "C:\docs\temperature.py", line 5
# SyntaxError: Non-ASCII character '\xe2' in file C:\docs\temperature.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
#
# changes commas to apostrophes in menu interface (lines 5-8). Code runs now.
