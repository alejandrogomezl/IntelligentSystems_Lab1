class Action:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __repr__(self):
        return f"Action({self.origin} -> {self.destination})"