from readJSON import loadJSON as ReadJson
from search import Search
from graph import GraphVisualizer as Graph

class Main:
    def __init__(self, json_file, algorithm, print=False):
        self.json_file = json_file
        self.algorithm = algorithm
        self.print = print

    def time_format(self, seconds):
        hours = int(seconds/3600)
        minutes = int(seconds/60)
        seconds = seconds%60
        return f'{hours}:{minutes}:{seconds}'
    
    def if_solution(self, solution_node, problem):
        if solution_node:
            print("Generated Nodes:", solution_node[1])
            print("Expanded Nodes:", solution_node[2])
            print("Solution Lenght:", solution_node[3])
            print("Solution Cost:", self.time_format(solution_node[4]))
            print("Execution Time:", self.time_format(solution_node[5]))
            print("Solution Path:", solution_node[0])
            if self.print: Graph(problem.intersections, problem.segments, solution_node[0]).show_graph()
            
        else:
            print("No se encontró solución")

    def run(self):
        problem = ReadJson(self.json_file)
        search = Search(problem)

        if self.algorithm == "bfs":
            print("Breadth First Search")
            self.if_solution(search.bfs(), problem)
        elif self.algorithm == "dfs":
            print("Depth First Search")
            self.if_solution(search.dfs(), problem)
        elif self.algorithm == "a":
            print("A* Search")
            self.if_solution(search.a_star, problem)
        elif self.algorithm == "best":
            print("Best First Search")
            self.if_solution(search.best_first(), problem)
        elif self.algorithm == "all":
            print("Breadth First Search")
            self.if_solution(search.bfs(), problem)
            print("\nDepth First Search")
            self.if_solution(search.dfs(), problem)
            print("\nA* Search")
            self.if_solution(search.a_star(), problem)
            print("\nBest First Search")
            self.if_solution(search.best_first(), problem)
            
        else:
            print("Invalid Algorithm")

        

if __name__ == "__main__":
    #Main("./problems/huge/calle_agustina_aroca_albacete_5000_0.json", "best", True).run()
    #Main("./problems/huge/calle_herreros_albacete_2000_2.json", "best", False).run()
    #Main("./problems/small/calle_del_virrey_morcillo_albacete_250_3.json", "a", True).run()
    Main("./problems/huge/paseo_simón_abril_albacete_5000_3.json", "all", False).run()