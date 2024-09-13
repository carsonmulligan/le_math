import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Define four colors
colors = ['red', 'blue', 'green', 'yellow']

# Create a sample graph to represent a map
def create_map_graph():
    """
    Creates a sample graph representing a map, where each node is a region, 
    and edges indicate adjacency between regions.
    """
    G = nx.Graph()
    
    # Add regions as nodes
    for i in range(1, 9):
        G.add_node(i)
    
    # Add edges to represent adjacency (shared borders between regions)
    edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4),
             (3, 5), (4, 5), (4, 6), (5, 6), (5, 7), 
             (6, 7), (7, 8), (5, 8), (6, 8)]
    G.add_edges_from(edges)
    
    return G

# Function to plot the graph and allow color interactions
def plot_map(G, node_colors=None):
    """
    Plots the graph using Plotly, with interactive color options for nodes (regions).
    """
    pos = nx.spring_layout(G)  # Position the nodes in a visually appealing way
    edge_x = []
    edge_y = []
    
    # Extract edge coordinates for Plotly
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
    
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='gray'),
        hoverinfo='none',
        mode='lines')
    
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
    
    # Default node colors if none provided
    if node_colors is None:
        node_colors = ['#FFFFFF'] * len(G.nodes())
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            colorscale='YlGnBu',
            color=node_colors,
            size=30,
            line_width=2))
    
    # Assign hover text with node information
    node_text = []
    for node in G.nodes():
        node_text.append(f"Region {node}")
    node_trace.text = node_text
    
    # Create the full figure
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<b>Interactive Map Coloring - Four-Color Theorem</b>',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        annotations=[dict(
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)]))
    
    fig.show()

# Function to assign colors while ensuring no two adjacent regions share the same color
def assign_colors(G):
    """
    Assign colors to the graph using the four-color theorem.
    Ensures no two adjacent nodes share the same color.
    """
    # Greedy coloring algorithm
    color_map = nx.coloring.greedy_color(G, strategy="largest_first")
    
    # Convert to a color format (using the predefined 4 colors)
    node_colors = []
    for node in G.nodes():
        color_index = color_map[node] % len(colors)  # Ensuring 4 colors max
        node_colors.append(colors[color_index])
    
    return node_colors

# Main execution
if __name__ == "__main__":
    G = create_map_graph()        # Create the map graph
    node_colors = assign_colors(G)  # Assign colors according to the four-color theorem
    plot_map(G, node_colors)        # Plot the graph with assigned colors
