from state import State

class Problem:
    def __init__(self, initial_state, goal_state, intersections, segments):
        """
        initial_state: Estado inicial (intersección de partida).
        goal_state: Estado objetivo (intersección de destino).
        graph: Grafo que representa las conexiones entre las intersecciones.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.intersections = (intersections)
        self.segments = segments

    def actions(self, state):
        """Returns the actions available from a given state."""
        return state.neighbors

    def result(self, state, action):
        """Returns the resulting state after taking an action."""
        return action.destination

    def goal_test(self, state):
        """Checks if the given state is the goal state."""
        return state == self.goal_state

    def path_cost(self, cost_so_far, state1, action, state2):
        """Returns the cost of a solution path that arrives at state2 from state1."""
        return cost_so_far + action.cost()
    
    def get_initial_state(self):
        return self.initial_state
    
    def is_goal(self, state):
        return state == self.goal_state
