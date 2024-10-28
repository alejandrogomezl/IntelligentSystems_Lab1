from readJSON import loadJSON as ReadJson
from search import Search
from graph import GraphVisualizer as Graph

class Main:
    def __init__(self, json_file, algorithm, print=False):
        self.json_file = json_file
        self.algorithm = algorithm
        self.print = print

    def run(self):
        problem = ReadJson(self.json_file)
        search = Search(problem)


        if self.algorithm == "breadth":
            solution_node = search.bfs()
        elif self.algorithm == "depth":
            solution_node = search.dfs()
        elif self.algorithm == "a":
            solution_node = search.a_star()
        elif self.algorithm == "best":
            solution_node = search.best_first()
        else:
            print("Not valid option: ", self.algorithm)
            return
        

        if solution_node:
            print("Generated Nodes:", solution_node[1])
            print("Expanded Nodes:", solution_node[2])
            print("Solution Depth:", solution_node[3])
            print("Solution Cost:", solution_node[4])
            print(f'Execution Time: {solution_node[5]*1000000000:.6f} nS')
            print("Solution Path:", solution_node[0])


            #Print the graph
            if self.print: Graph(problem.intersections, problem.segments, solution_node[0]).show_graph()

        else:
            print("No se encontró solución")

if __name__ == "__main__":
    Main("./problems/huge/calle_agustina_aroca_albacete_5000_0.json", "depth", False).run()