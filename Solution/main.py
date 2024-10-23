from readJSON import JsonReader
from search import Search
from problem import Problem
from graph import GraphVisualizer

#file = "./problems/small/calle_agustina_aroca_albacete_250_0.json"
file = "./problems/small/calle_del_virrey_morcillo_albacete_250_3.json"


initial_state, goal_state, intersections, segments = JsonReader(file)
problem = Problem(initial_state, goal_state, intersections, segments)

path = Search.bfs(problem)
