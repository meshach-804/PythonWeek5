# Activity 2: Polymorphism Challenge! 

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling along the path 🚴"
