import networkx as nx
import matplotlib.pyplot as plt

def calculateTotalCost(G):
    return sum(nx.get_edge_attributes(G, 'weight').values())
def plotGraph(G,pos=None, label=None):
    if pos is None:
        pos = nx.spring_layout(G, seed=42, scale=2)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', edge_color='red', linewidths=1, font_family='arial')
    if label:
        plt.title(label)
    plt.show()
    
    pos = nx.spring_layout(G, seed=42, scale=3)  # Adjust the scale parameter
    edge_weights = nx.get_edge_attributes(G, 'weight')
    """ edge_widths = [weight * 0.1 for weight in edge_weights.values()] """
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=14, font_color='black', font_weight='bold', edge_color='red', linewidths=3, font_family='arial')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.show()
    # Create an undirected graph representing the antennas
G = nx.Graph() # Use Graph instead of DiGraph
    # Add edges and their weights to the graph
edges = [

('A', 'C', {'weight': 13}),
('A', 'E', {'weight': 14}),
('A', 'D', {'weight': 9}),
('C', 'B', {'weight': 17}),
('B', 'D', {'weight': 13}),
('B', 'E', {'weight': 16}),
('C', 'E', {'weight': 10}),
('D', 'F', {'weight': 16}),
('G', 'E', {'weight': 12}),
('A', 'B', {'weight': 2}),
]
G.add_edges_from(edges)
# Plot the original undirected graph
plotGraph(G)

# Kruskal's Algorithm
kruskal_tree = nx.minimum_spanning_tree(G, algorithm='kruskal')
pos = nx.spring_layout(kruskal_tree)
plotGraph(kruskal_tree, pos, f'Kruskal\'s Algorithm (Cost: {calculateTotalCost(kruskal_tree)})')

# Prim's Algorithm
prim_tree = nx.minimum_spanning_tree(G, algorithm='prim')
pos = nx.spring_layout(prim_tree)
plotGraph(prim_tree, pos, f'Prim\'s Algorithm (Cost: {calculateTotalCost(prim_tree)})')

# Boruvka's Algorithm
boruvka_tree = nx.minimum_spanning_tree(G, algorithm='boruvka')
pos = nx.spring_layout(boruvka_tree)
plotGraph(boruvka_tree, pos, f'Boruvka\'s Algorithm (Cost: {calculateTotalCost(boruvka_tree)})')