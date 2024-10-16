import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío usando NetworkX
G = nx.Graph()

# Añadir nodos y aristas al grafo según las conexiones de la imagen
edges = [
    ("Arad", "Zerind"),
    ("Arad", "Sibiu"),
    ("Arad", "Timisoara"),
    ("Zerind", "Oradea"),
    ("Oradea", "Sibiu"),
    ("Timisoara", "Lugoj"),
    ("Lugoj", "Mehadia"),
    ("Mehadia", "Dobreta"),
    ("Dobreta", "Craiova"),
    ("Craiova", "Rimnicu Vilcea"),
    ("Craiova", "Pitesti"),
    ("Rimnicu Vilcea", "Sibiu"),
    ("Rimnicu Vilcea", "Pitesti"),
    ("Sibiu", "Fagaras"),
    ("Fagaras", "Bucharest"),
    ("Pitesti", "Bucharest"),
    ("Bucharest", "Giurgiu"),
    ("Bucharest", "Urziceni"),
    ("Urziceni", "Hirsova"),
    ("Hirsova", "Eforie"),
    ("Urziceni", "Vaslui"),
    ("Vaslui", "Iasi"),
    ("Iasi", "Neamt")
]

# Añadir las aristas al grafo
G.add_edges_from(edges)

# Dibujar el grafo
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Usamos un layout para distribuir los nodos

# Dibujar los nodos y las aristas
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")

# Mostrar la gráfica
plt.title("Mapa de ciudades")
plt.show()
