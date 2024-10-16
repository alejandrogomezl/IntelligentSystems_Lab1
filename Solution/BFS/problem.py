from state import State
from action import Action

class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = State(initial)
        self.goal = State(goal)
        self.graph = graph

    def actions(self, state):
        neighbors = self.graph[state.name]
        print(f"Acciones posibles desde {state.name}: {neighbors}")
        return [Action(state.name, neighbor) for neighbor in neighbors]

    def result(self, state, action):
        print(f"Aplicando acción: {action}")
        return State(action.destination)

    def goal_test(self, state):
        is_goal = state == self.goal
        print(f"¿Estado actual ({state.name}) es el objetivo ({self.goal.name})? {'Sí' if is_goal else 'No'}")
        return is_goal

    def step_cost(self, state, action):
        print(f"Costo de moverse de {action.origin} a {action.destination}: 1")
        return 1