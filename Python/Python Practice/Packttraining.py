#This is the notes on the beginning pythong course
#Section 1 is a basic overview in programming and setting up python
# The following are the basic commands in section 1

print('Hello World')
'''Variables are datapoints that can store a value. It is good practice to make variable in camElCase
so that they do not get confused with system variable'''

nAme = "Zubair"
print(nAme)

#The following is in section 2
# This section deals with strings and their manipulation

#Single and double quote strings. This helps usine single or double quote in a string
#Example is below

sen1 = 'I "really" like chocalate'
print(sen1)
sen2 = 'i \'really\' like milk also'
print(sen2)
sen3 = '''This is another way to write variable'''
print(sen3)

#The string API hels manipulate strings. We will change a string to upper

print(sen1.upper())
print(sen2.capitalize())
print(sen3.title())

space = '         blank space        '
print(space.strip().upper())

prefix = "python is an"
suffix = "awsome language"

new = prefix+suffix

print(new)

new = new.replace("language", "snake")

print(new)

new = new * 2

new = new.replace("snake", "language", 1)

print(new)
print(new.count("an"))


#The following deals with string formating

n = 11
f = 1.2345678
s = "computer"

print("my number is {:d}".format(n))
print("my number is {:b}".format(n))

'''We can use many formats. e for exponents, b binary,
o octal, d decimal, x hexadecimal, f float,
s string (This is default)'''

print("{:11.3f}".format(f))
print("{:011.3f}".format(f))

print("{0} {1} {2}".format(n,f,s))

print("{name} has a total of {amount} of {object}".format(
    name = "Zubair",
    amount = 5.6,
    object = "Apples"
))

#User input methods and uses

first_name  = str(input("Please enter your First name? "))
middle_name  = str(input("Please enter your Middle name? "))
last_name  = str(input("Please enter your Last name? "))

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s} {last}"

print(first_name)
print(middle_name)
print(last_name)

print(name_format.format(first=first_name, middle=middle_name, last=last_name))


#Section 3. Dealing with lists

numbers = [5, -6, 2, 4, -5, 1]
names = ["Heather", "Micah", "Jane"]

print(names[0])
print(names[1])
print(names[2])

del names[1]

print(names)

names.append("Zubair")
names = names + ["Huma"]
names.remove("Jane")
print(names)
z_index = names.index("Zubair")
print(z_index)




#A variable cannot start with a number. We can however have a variable starting with an underscore.
_name = "Zukhiro"
print(_name)

'''Types in python. A string type can be anything. While an integer type is a whole numnber.
These can be very long. You can also have a float which is a number with decimalsself.
How every python will only keep a certian decimal points and this is not infinite.'''

#How to convert between integer or float

nUm1 = 3.4
nUm2 = 3.9

print(int(nUm1))
print(float(3))
