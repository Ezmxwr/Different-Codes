""" import networkx as nx
import matplotlib.pyplot as plt
# Function to plot the original directed graph
def plotGraph(G):
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray', linewidths=1, font_family='arial', arrowsize=10)
    plt.title('Original Directed Graph')
    plt.show()
    # Create a directed graph representing the network
G = nx.DiGraph()
# Add edges and their weights to the graph
edges = [
('User', 'Kuwait', {'weight': 2}),
('User', 'UAE', {'weight': 13}),
('User', 'Oman', {'weight': 17}),
('User', 'Qatar', {'weight': 2}),
('User', 'Bahrain', {'weight': 9}),
('User', 'KSA', {'weight': 7}),
('Qatar', 'Kuwait', {'weight': 13}),
('Bahrain', 'Oman', {'weight': 14}),
('Oman', 'KSA', {'weight': 12}),
('UAE', 'KSA', {'weight': 19}),
('UAE', 'Bahrain', {'weight': 16}),
]

G.add_edges_from(edges)
# Plot the original directed graph
plotGraph(G)
#------ """

import networkx as nx
import matplotlib.pyplot as plt


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
    
G = nx.DiGraph()
# Add nodes
G.add_node('Qatar')
G.add_node('Kuwait')
G.add_node('Bahrain')
G.add_node('Oman',pos=(0,2))
G.add_node('UAE',pos=(0,2))
G.add_node('KSA')
G.add_node('User')

# Add edges
G.add_edge('Kuwait', 'Qatar', weight=13)
G.add_edge('Qatar', 'User', weight=2)
G.add_edge('User', 'Kuwait', weight=16)
G.add_edge('User', 'UAE', weight=13)
G.add_edge('Bahrain', 'User', weight=9)
G.add_edge('KSA', 'User', weight=7)
G.add_edge('KSA', 'UAE', weight=19)
G.add_edge('UAE', 'KSA', weight=19)
G.add_edge('KSA', 'Oman', weight=12)
G.add_edge('User', 'Oman', weight=17)
G.add_edge('Oman', 'Bahrain', weight=14)
G.add_edge('UAE', 'Bahrain', weight=16)


# Set positions for the nodes
pos = nx.spring_layout(G)

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=500,node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=1, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
nx.draw_networkx_labels(G, pos, font_size=16, font_family='sans-serif',font_color='red')

# Show the plot
plt.axis('off')
plt.show()
