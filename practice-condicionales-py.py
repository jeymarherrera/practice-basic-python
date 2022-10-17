edad = 30

if edad < 20 :
  print("su edad es menor de 20")  
else:
    print("su edad es mayor de 20")

color = "blue"

if color == "red":
    print("el color es red")
elif color == "blue":
    print("el color es blue")
else:
    print("el color no es rojo, ni blue")

name = "Jey"
lastname = "Carter"

if name == "Jey":
    if lastname == "Carter":
        print ("Eres el usuario")
    else:
        print("No eres el usuario Jey Carter")
else:
    print("No eres el usuario Jey")

x=5
y=5
if x > 2 and x <= 10:
    print("x es mayor que 2 y menor igual que 10")
if x > 2 or x <=20:
    print("x es mayor que 2 y menor igual a 20")
if (not(x==y)):
    print("x no es igual que x")
        