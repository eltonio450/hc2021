class Car:
    def __init__(self, path):
        self.timeToRedLight = 0
        self.remaining = path

class Street:
    def __init__(self, start, end, length, cars):
        self.start = start
        self.end = end
        self.cars = cars
        self.length = length

    def removeCar(self):
        if(len(self.cars) >0):
            self.cars = self.cars[1:]
        self.cars = []



class Intersection :
    def __init__(self):
        self.allowedStreet = None


    def turnGreen(self, incomingStreet):
        self.allowedStreet = incomingStreet


## intersections in a dictionary of intersections
# green light is a representation of the green lights
class Model:
    def __init__(self, duration, intersections, streets, cars):
        self.duration = duration
        self.intersections = intersections # dictionary of intersections
        self.streets = streets
        self.cars = cars

    def step(self, greenLights):
            # turn green 