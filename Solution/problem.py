from state import State
from action import Action

class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = State(initial)
        self.goal = State(goal)
        self.graph = graph

    def actions(self, state):
        neighbors = self.graph[state.name]
        return [Action(state.name, neighbor) for neighbor in neighbors]

    def result(self, state, action):
        return State(action.destination)

    def goal_test(self, state):
        is_goal = state == self.goal
        return is_goal

    def step_cost(self, state, action):
        return 1