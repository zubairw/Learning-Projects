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

num1 = int(input("Fist Number"))
print(num1)
num2 = int(input("Second Number"))
print(num2)

num3 = num1 + num2
print(num3)