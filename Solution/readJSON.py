import json
from state import State
from action import Action

def JsonReader(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    intersections = {}
    for i_data in data["intersections"]:
        inter = State(
            id=i_data["identifier"],
            latitude=i_data["latitude"],
            longitude=i_data["longitude"],
        )
        intersections[inter.id] = inter

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
        # Add neighbors to the origin state
        origin.neighbors.append((destination, segment))

    for state in intersections.values():
        state.neighbors.sort(key=lambda x: x[0].id, reverse=True)

    initial_state = intersections[data["initial"]]
    goal_state = intersections[data["final"]]

    return initial_state, goal_state, intersections, segments
