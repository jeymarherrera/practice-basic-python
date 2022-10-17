myStr = "Hello World"
#funcion que indica otra funciones que puedo realizar al string
#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.capitalize())
print(myStr.swapcase())

print(myStr.replace('Hello', 'bye'))
print(myStr.replace('Hello', 'bye').upper())
print(myStr.count('l'))
print(myStr.startswith('hola'))
print(myStr.endswith('World'))
print(myStr.split())
print(myStr.split('l'))
print(myStr.find('o'))

print(len(myStr))
print(myStr.index('e'))

print(myStr.isalnum())
print(myStr.isalpha())
print(myStr.isspace())
print(myStr[4])
print(myStr[-4])

print(myStr + " Como estas")
print(f"Saludo a {myStr}")
print(" Como estas {0}".format(myStr))