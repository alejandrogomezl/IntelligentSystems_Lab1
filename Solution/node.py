class Node:
    def __init__(self, state, parent=None, depth=0, cost=0):
        """
        state: Estado representado por un identificador de intersección.
        parent: Nodo desde el cual se llegó a este nodo.
        depth: Nivel del nodo (profundidad en el árbol de búsqueda).
        cost: Costo acumulado hasta este nodo (opcional, útil para A*).
        """
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
        self.cost = cost
    
    def __eq__(self, other):
        """
        Dos nodos son iguales si tienen el mismo estado.
        """
        if isinstance(other, Node):
            return self.state == other.state
        return False
    
    def __hash__(self):
        """
        Permite que los nodos sean utilizados en conjuntos y como claves en diccionarios.
        """
        return hash(self.state)
    
    def __repr__(self):
        """
        Representación amigable del nodo, mostrando su estado y profundidad.
        """
        return f"Node(state={self.state}, depth={self.depth}, cost={self.cost})"
    
    def expand(self, problem):
        """
        Expande el nodo generando los hijos, es decir, los estados sucesores.
        """
        return [Node(next_state, self, self.depth + 1) for next_state in problem.get_successors(self.state)]
    
    def path(self):
        """
        Reconstruye el camino desde el estado inicial hasta el nodo actual.
        """
        node, path_back = self, []
        while node:
            path_back.append(node.state.identifier)
            node = node.parent
        return list(reversed(path_back))
