import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

def plotGraph(G, pos=None, label=None):
    if pos is None:
        pos = nx.spring_layout(G, seed=78, scale=1)
    nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', edge_color='red', linewidths=1, font_family='arial')
    if label:
        plt.title(label)
    
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.show() 

def floyd_warshall_table(graph):
    nodes = graph.nodes()
    floyd_warshall_distances = nx.floyd_warshall_numpy(graph, weight='weight', nodelist=nodes)

    # Create a DataFrame for the results
    df_floyd_warshall = pd.DataFrame(floyd_warshall_distances, index=nodes, columns=nodes)

    # Display the results as a table
    print("\nFloyd-Warshall Distances:")
    table_floyd_warshall = tabulate(df_floyd_warshall, headers='keys', tablefmt='grid')
    print(table_floyd_warshall)

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


floyd_warshall_distances = nx.floyd_warshall_numpy(G, weight='weight', nodelist=nodes)
# Display the distances

user_distances_bellman_ford = nx.single_source_bellman_ford_path_length(G, source='User', weight='weight')


# Apply Floyd-Warshall and display the results
floyd_warshall_table(G)

# Calculate the distances from the user to all other servers using Dijkstra's algorithm
user_distances_dijkstra = nx.single_source_dijkstra_path_length(G, source='User', weight='weight')
df_dijkstra = pd.DataFrame(list(user_distances_dijkstra.items()), columns=['Edges', 'Cost'])
df_bellman_ford = pd.DataFrame(list(user_distances_bellman_ford.items()), columns=['Edges', 'Cost'])
custom_order = ['User', 'Kuwait', 'UAE', 'Oman', 'Qatar', 'Bahrain', 'KSA']

# Convert 'Edges' column to Categorical with custom order
df_dijkstra['Edges'] = pd.Categorical(df_dijkstra['Edges'], categories=custom_order, ordered=True)
df_bellman_ford['Edges'] = pd.Categorical(df_bellman_ford['Edges'], categories=custom_order, ordered=True)
# Sort the DataFrame by the 'Edges' column
df_dijkstra_sorted = df_dijkstra.sort_values('Edges')
df_bell_sorted = df_bellman_ford.sort_values('Edges')

# Display the sorted DataFrame
print("\nDijkstra Distances:")
table_dijkstra = tabulate(df_dijkstra_sorted, headers='keys', tablefmt='grid', showindex=False)
print(table_dijkstra)
print("\nBell Distances:")
table_Bell = tabulate(df_bell_sorted, headers='keys', tablefmt='grid', showindex=False)
print(table_Bell)


# Compare the results
print("\nComparison of Dijkstra and Bellman Ford:")
for i, node in enumerate(nodes):
    dijkstra_distance = user_distances_dijkstra[node]
    bellman_ford_distance= user_distances_bellman_ford[node]
    print(f"{node}: Dijkstra - {dijkstra_distance}, Bellman Ford - {bellman_ford_distance}, Difference - {dijkstra_distance - bellman_ford_distance}")
    
print("\nComparison of Dijkstra and Floyd-Warshall:")
for i, node in enumerate(nodes):
    dijkstra_distance = user_distances_dijkstra[node]
    floyd_warshall_distance = floyd_warshall_distances[nodes.index('User')][nodes.index(node)]
    print(f"{node}: Dijkstra - {dijkstra_distance}, Floyd-Warshall - {floyd_warshall_distance}, Difference - {dijkstra_distance - floyd_warshall_distance}")
pos = nx.spring_layout(G)
