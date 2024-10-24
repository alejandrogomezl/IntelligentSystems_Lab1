from readJSON import loadJSON as ReadJson
from search import Search

class Main:
    def __init__(self, json_file):
        self.json_file = json_file

    def run(self):
        # 1. Leer el archivo JSON y obtener el grafo
        problem = ReadJson(self.json_file)
       
        # 4. Crear una instancia de Search y ejecutar BFS
        search = Search(problem)
        solution_node = search.best_first()

        # 5. Imprimir los resultados
        if solution_node:
            print("Camino encontrado:", solution_node)
        else:
            print("No se encontró solución")

# Ejecutar el programa
if __name__ == "__main__":
    # Instancia de la clase Main con el archivo JSON
    Main("./problems/small/calle_del_virrey_morcillo_albacete_250_3.json").run()
    #Main("./problems/huge/calle_agustina_aroca_albacete_5000_0.json").run()
