import json
from state import State
from action import Action
from problem import Problem


def loadJSON(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    intersections = {}
    for i_data in data["intersections"]:
        inter = State(
            identifier=i_data["identifier"],
            latitude=i_data["latitude"],
            longitude=i_data["longitude"],
        )
        intersections[inter.identifier] = inter

    segments = []
    for seg_data in data["segments"]:
        origin = intersections[seg_data["origin"]]
        destination = intersections[seg_data["destination"]]
        segment = Action(
            origin=origin,
            destination=destination,
            distance=seg_data["distance"],
            speed=seg_data["speed"],
        )
        segments.append(segment)
        origin.neighbors.append((destination, segment))

    initial_state = intersections[data["initial"]]
    goal_state = intersections[data["final"]]



    def heuristic(self, state, goal):
        x = state.latitude - goal.latitude
        y = state.longitude - goal.longitude
        return (x**2 + y**2)**0.5

    for state in intersections.values():
        # state.neighbors.sort(key=lambda x: x[0].identifier, reverse=False)
        #Probar usar euristica para ordenar los nodos
        state.neighbors.sort(key=lambda x: heuristic(x[0], goal_state), reverse=False)


    return Problem(initial_state, goal_state, intersections, segments)

