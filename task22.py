

import networkx as nx
import matplotlib.pyplot as plt

def plotGraph(G,pos=None, label=None):
    if pos is None:
        pos = nx.spring_layout(G, seed=78, scale=1)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', edge_color='red', linewidths=1, font_family='arial')
    if label:
       plt.title(label)
    
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.show() 
G = nx.DiGraph()
nodes = ['Qatar', 'Kuwait', 'Bahrain', 'Oman', 'UAE', 'KSA', 'User']
G.add_nodes_from(nodes)

edges = [
    ('Kuwait', 'Qatar', {'weight': 13}),
    ('Qatar', 'User', {'weight': 2}),
    ('User', 'Kuwait', {'weight': 16}),
    ('User', 'UAE', {'weight': 13}),
    ('Bahrain', 'User', {'weight': 9}),
    ('KSA', 'User', {'weight': 7}),
    ('KSA', 'UAE', {'weight': 19}),
    ('UAE', 'KSA', {'weight': 19}),
    ('KSA', 'Oman', {'weight': 12}),
    ('User', 'Oman', {'weight': 17}),
    ('Oman', 'Bahrain', {'weight': 14}),
    ('UAE', 'Bahrain', {'weight': 16}),
]
G.add_edges_from(edges)
plotGraph(G)


user_distances = nx.single_source_dijkstra_path_length(G, source='User', weight='weight')

# Display the distances
print("Using dijkstra")
for server, distance in user_distances.items():
    print(f" Distance from User to {server}: {distance}")

user_distances = nx.single_source_bellman_ford_path_length(G, source='User', weight='weight')

print("Using bellman ford")
# Display the distances
for server, distance in user_distances.items():
    print(f"Distance from User to {server}: {distance}")


####
floyd_warshall_distances = nx.floyd_warshall_numpy(G, weight='weight')

print("Floyd-Warshall Distances:")
for i, node in enumerate(nodes):
    print(f"From User to {node}: {floyd_warshall_distances[i][-1]}")

# Calculate the distances from the user to all other servers using Dijkstra's algorithm
user_distances_dijkstra = nx.single_source_dijkstra_path_length(G, source='User', weight='weight')

# Display the results as a table
print("\nDijkstra Distances:")
for node, distance in user_distances_dijkstra.items():
    print(f"From User to {node}: {distance}")

# Compare the results
print("\nComparison of Dijkstra and Floyd-Warshall:")
for i, node in enumerate(nodes):
    dijkstra_distance = user_distances_dijkstra[node]
    floyd_warshall_distance = floyd_warshall_distances[i][-1]
    print(f"{node}: Dijkstra - {dijkstra_distance}, Floyd-Warshall - {floyd_warshall_distance}, Difference - {dijkstra_distance - floyd_warshall_distance}")

pos = nx.spring_layout(G)


