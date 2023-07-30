class Dog:

    dogInfo = "Hey dogs are cool"

    def bark(self):
        print("BARK!")

    def bark_text(str):
        print("BARK!" + str)


mydog = Dog()
mydog.bark()

mydog.name = "Fido"
mydog.age = "10"
print(mydog.name)
print(mydog.age)
print(Dog.dogInfo)

Dog.dogInfo = "Hey there"
print(Dog.dogInfo)
Dog.bark_text("BARK!")


## The init method lets you set instance variable

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    ## To use this function you need to create all the instance variables
    def age(self):
        return 2020 - self.year



Mycar = Car(2016, "Hyundai", "Creta")
print(Mycar.age())


