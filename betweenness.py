
import random
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap, Normalize
import igraph as ig


def plot_betweenness(g, vertex_betweenness, edge_betweenness, ax, cax1, cax2):
    '''Plot vertex/edge betweenness, with colorbars

    Args:
        g: el grafo a trazar.
        ax: los ejes para el gráfico
        cax1: los ejes para la barra de color de la centralidad de los vértices
        cax2: los ejes para la barra de color de la centralidad de las aristas
    '''

    # Reescalar la centralidad para que esté entre 0.0 y 1.0
    scaled_vertex_betweenness = ig.rescale(vertex_betweenness, clamp=True)
    scaled_edge_betweenness = ig.rescale(edge_betweenness, clamp=True)
    print(f"vértices: {min(vertex_betweenness)} - {max(vertex_betweenness)}")
    print(f"aristas: {min(edge_betweenness)} - {max(edge_betweenness)}")

    # Definir mapeos centralidad -> color
    cmap1 = LinearSegmentedColormap.from_list("vertex_cmap", ["pink", "indigo"])
    cmap2 = LinearSegmentedColormap.from_list("edge_cmap", ["lightblue", "midnightblue"])

    # Trazar el grafo
    g.vs["color"] = [cmap1(betweenness) for betweenness in scaled_vertex_betweenness]
    g.vs["size"]  = ig.rescale(vertex_betweenness, (10, 50))
    g.es["color"] = [cmap2(betweenness) for betweenness in scaled_edge_betweenness]
    g.es["width"] = ig.rescale(edge_betweenness, (0.5, 1.0))
    ig.plot(
        g,
        target=ax,
        layout="fruchterman_reingold",
        vertex_frame_width=0.2,
    )

    # Barras de color
    norm1 = ScalarMappable(norm=Normalize(0, max(vertex_betweenness)), cmap=cmap1)
    norm2 = ScalarMappable(norm=Normalize(0, max(edge_betweenness)), cmap=cmap2)
    plt.colorbar(norm1, cax=cax1, orientation="horizontal", label='Centralidad de los Vértices')
    plt.colorbar(norm2, cax=cax2, orientation="horizontal", label='Centralidad de las Aristas')

#grafo derecho
random.seed(12)#genera enteros aleatorios
g1 = ig.Graph.Famous("Krackhardt_Kite")

vertex_betweenness1 = g1.betweenness()
edge_betweenness1 = g1.edge_betweenness()

g2 = ig.Graph.Watts_Strogatz(dim=1, size=150, nei=2, p=0.1)
vertex_betweenness2 = g2.betweenness()
edge_betweenness2 = g2.edge_betweenness()

fig, axs = plt.subplots(
    3, 2,
    figsize=(7, 6),
    gridspec_kw={"height_ratios": (20, 1, 1)},
)
plot_betweenness(g1, vertex_betweenness1, edge_betweenness1, *axs[:, 0])
plot_betweenness(g2, vertex_betweenness2, edge_betweenness2, *axs[:, 1])
fig.tight_layout(h_pad=1)
plt.show()
