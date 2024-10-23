class State:
    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.neighbors = []

    def __eq__(self, other):
        return isinstance(other, State) and self.id == other.id

    def __hash__(self):
        return hash(self.id)