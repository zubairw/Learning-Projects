''' The following are basic python commands '''

print('Hello')
print('This is a test')
### This is a basic print statement

varOne = "This is my first Variable"

## This is a basic string variable

print(varOne)

## We can also perform math functions

strOne = 100

print(strOne)
print(strOne / 5)

## We cannot create variables starting with a number. We can put an _ before a variable to start with a number

_100test = strOne / 2.3
print(_100test)

## While Loops create conditional code.

condition = 1

while condition <= 10:
   print(condition)
   condition += 1

## For Loops are similar to while loop. They are used with lists mostly

expList = [1, 6, 7, 3, 6, 9, 0]

for x in expList:
   print(x)

for y in range(1, 11):
   print(y)

## If statements are also conditional statement. We can have ==, >, <, <=, >=,

x = 2
y = 7
z = 10

if x > y and y > z:
   print('Yahoo')
else:
   print('NNNNOOOOOOOOO')

if x < y and y < z:
   print('Its True')
else:
   print('Not true')

if x == y and x <= z:
   print('Nothing')

if x < y < z:
   print('Its all trure. i checked')

if x > y or y > z:
   print('x > y')
elif x < y and y < z:
   print('x < y')

''' The following is an example for class structure and possible uses '''


def func1():
   x=1
   y=3
   print(x+y)

func1()

def addition(num1,num2):
   ans = num1+num2
   return ans

x = addition(5,6)
print(x)

a = int(input("Enter number 1?"))
b = int(input("Enter numebr 2?"))
c = addition(a,b)
print(c)

def web(font,fonts,bgcol,fontcol):
   print(font)
   print(fonts)
   print(bgcol)
   print(fontcol)

web(fonts=2,
   font="TNR",
   bgcol="White",
   fontcol="Black")

for x in range(1,6):
    print("I want to go to the park. This is what Yahya wants")
    print(x)
