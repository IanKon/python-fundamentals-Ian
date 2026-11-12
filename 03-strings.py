# Strings
string = "Kenny-Ola"
print(string)
string = "Some text"
print(string.upper())

## indexing
print(string[0])
print(string[-1])

## slice
print(string[0:4])
print(string[5:])

## length
print(len(string))

## concatenation (f-strings)
name = "Ian"
age = 18
print("Hello, " + name)
print(f"{name} is {age} years old")

## uppercase / lowercase / title / strip
messy = "  hello world  "
print(messy.upper())
print(messy.lower())
print(messy.title())
print(messy.strip())

## find()
print(string.find("text"))
print(string.find("xyz"))