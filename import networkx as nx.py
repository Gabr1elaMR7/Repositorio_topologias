import networkx as nx
import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# Crear un grafo bipartito vacío
G_peliculas_actores = nx.Graph()
#G_peliculas_Secuelas = nx.graph()
# Agregar los nodos de cada grupo
G_peliculas_actores.add_nodes_from(["Pelicula_1", "Pelicula_2", "Pelicula_3"], bipartite="Peliculas")
G_peliculas_actores.add_nodes_from(["Secuela_1"], bipartite="Secuelas")
G_peliculas_actores.add_nodes_from(["Actor_1", "Actor_2", "Actor_3"], bipartite="Actores")

# Agregar las relaciones entre los nodos
G_peliculas_actores.add_edges_from(
    [
        ("Pelicula_1", "Actor_1","secuela_1"),
        ("Pelicula_2", "Actor_2"),
        ("Pelicula_3", "Actor_3"),
        ("Pelicula_2", "Actor_3"),
        ("Pelicula_2", "Actor_1"),
    ]
)

# Se identifican los nodos del conjunto de interés
nodes_bipartite = [
    n[0]
    for n in G_peliculas_actores.nodes(data=True)
    if n[1]["bipartite"] == "Actores"
]

# Proyección del grafo bipartito para obtener sólo los nodos del grupo de actores
G_actores = nx.bipartite.projected_graph(G_peliculas_actores, nodes_bipartite)

# colores para cada tipo de nodo en el grafo bipartito
colores = {"Peliculas": "red", "Actores": "blue","Secuelas":"green"}
colores_nodos = [colores[n[1]["bipartite"]] for n in G_peliculas_actores.nodes(data=True)]

fig, ax = plt.subplots(figsize=(5, 4))
nx.draw(
    G_peliculas_actores,
    pos=nx.spring_layout(G_peliculas_actores),
    with_labels=True,
    node_color=colores_nodos,
    ax=ax,
)

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G_actores, with_labels=True, ax=ax)
ax.set_xlim([1.2 * x for x in ax.get_xlim()])
ax.set_ylim([1.2 * y for y in ax.get_ylim()])

plt.show()
