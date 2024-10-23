class Problem:
    def __init__(self, initial, goal, intersections, segments):
        self.initial = initial
        self.goal = goal
        self.intersections = intersections
        self.segments = segments

    def actions(self, state):
        return state.neighbors

    def result(self, satate, action):
        return action.destination
    
    def goal_test(self, state):
        return state == self.goal

    def step_cost(self, state_cost, action_cost):
        return state_cost + action_cost()