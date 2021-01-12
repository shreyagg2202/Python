class Animal:
    def Dog(self):
        print("Dog is barking")

class AnimalChild(Animal):
    def DogChild(self):
        print("Dog's child is eating")

class Cal(AnimalChild):
    def Add(self):
        n1=2
        n2=3
        print(n1+n2)

        
obj = Cal()          #Always create object of child
obj.Dog()
obj.DogChild()
obj.Add()

