foods = ['apples', 'bread', 'cheese', 'milk', 'bananas', 'graves']

for food in foods:
    if food == "cheese":
        print("you have to buy this")
    print(food)

print("\n")

for food in foods:
    if food == "cheese":
        break
    print(food)

print("\n")

for food in foods:
    if food == "cheese":
        continue
    print(food)

print("\n")

for number in range (1,8):
    print(number)

print("\n")

for letter in "Hello":
    print(letter)

print("\n")

count = 4
while count <= 10:
    print(count)
    count = count + 1

print("\n")