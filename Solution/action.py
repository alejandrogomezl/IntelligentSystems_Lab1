class Action:
    def __init__(self, origin, destination, distance, speed):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        self.speed = speed/3.6

    def cost(self):
        return self.distance / self.speed