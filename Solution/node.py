class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0 if parent is None else parent.depth + 1

    def path(self):
        path = []
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        path.reverse()
        return path