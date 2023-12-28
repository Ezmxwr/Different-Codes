
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
