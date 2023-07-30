age = 15

name = "Luis"

todayIsCold = True

# this is a comment
"""This is a multiline comment
This will not execute"""

if age > 18:
    print("You are older than 13")
    print("this is another line")
else:
    print("You are younger than 18")

year = 2021

if 2000 <= year < 2099:
    print("Welcome to the 21st century!")
else:
    print("You are before or after the 21st century")


def hello():
    print("hello world")


hello()
hello()
hello()


def tripleprint(text):
    print(text * 3)


dog_names = ['torvi', 'chivo']

print(dog_names)

dog_names.insert(0, 'paris')

print(dog_names)

dog_names.insert(3, 'fancy')

print(dog_names)

del(dog_names[3])

shoes = ['Spizikes', 'Air Force 1', 'Curry 2', 'Melo 5']

for i in range(1, 112):
    print(i)

while age < 18:
    print(age)
    age += 1

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70,
           81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39,
           58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18,
           98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for i in numbers:
    if i > 90:
        print(i)


dogs = {"Torvi" : 2, "Chivo" : 11, "Paris" : 14}

print(dogs['Chivo'])

del(dogs['Paris'])

dogs["Negrita"]=1


print(dogs)

words = ["PoGo", "Spange", "Lie-Fi"]
definitions = ["Slang for Pokemon Go",
               "To collect spare change, either from couches, passerbys on the street or any numerous other ways and means",
               "When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = {}

for i in range(0,3):
    cooldictionary[i] = definitions[i]

print(cooldictionary)