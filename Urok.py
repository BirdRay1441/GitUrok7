class Car:
    def __init__(self, color, brend, speed):
        self.color = color
        self.brend = brend
        self.distance = 50
        self.speed = speed
    def __str__(self):
        return f'Car({self.brend}, {self.color}); Distance = {self.distance}'

    def update(self):
        self.distance += self.speed*2


Mazda = Car('Red', "Mazda", 30)

Mazda.update()
Mazda.update()

print(Mazda.distance)

