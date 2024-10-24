from readJSON import loadJSON as ReadJson
from search import Search

class Main:
    def __init__(self, json_file, algorithm):
        self.json_file = json_file
        self.algorithm = algorithm

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
            print("Algoritmo no válido")
            return
        

        if solution_node:
            print("Camino encontrado:", solution_node)
        else:
            print("No se encontró solución")

# Ejecutar el programa
if __name__ == "__main__":
    # Instancia de la clase Main con el archivo JSON
    #Main("./problems/small/calle_del_virrey_morcillo_albacete_250_3.json").run()
    #Main("./problems/huge/calle_agustina_aroca_albacete_5000_0.json").run()
    Main("./problems/small/calle_agustina_aroca_albacete_250_0.json", "breadth").run()