import networkx as nx
import plotly.graph_objects as go
import numpy as np
import random

# Define four colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']  # Red, Blue, Green, Yellow
color_names = ['Red', 'Blue', 'Green', 'Yellow']

# Create a complex map graph with random node connections
def create_complex_map(num_nodes, edge_probability=0.3):
    """
    Creates a random graph representing a map, where each node is a region, 
    and edges indicate adjacency between regions. 
    """
    G = nx.gnp_random_graph(num_nodes, edge_probability)
    return G

# Function to plot the graph and allow color interactions
def plot_map(G, node_colors):
    """
    Plots the graph using Plotly, with interactive color options for nodes (regions).
    The graph allows manual color changing.
    """
    pos = nx.spring_layout(G)  # Position the nodes using spring layout (for nicer visuals)
    
    # Extract edges for Plotly
    edge_x = []
    edge_y = []
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
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines')

    # Plot nodes (regions)
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=[colors[node_colors[node]] for node in G.nodes()],  # Assign initial colors
            size=20,
            line_width=2))

    # Assign hover text with node information
    node_text = []
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        adj_info = f"Region {node + 1}, Adjacent to: {', '.join(map(str, [n + 1 for n in neighbors]))}"
        node_text.append(adj_info)
    node_trace.text = node_text

    # Create the figure
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
                            x=0.005, y=-0.002)],
                        updatemenus=[
                            {
                                'buttons': [
                                    {
                                        'args': [{'marker.color': [colors[i % len(colors)] for i in node_colors]}],
                                        'label': 'Recolor',
                                        'method': 'restyle'
                                    }
                                ],
                                'direction': 'down',
                                'pad': {'r': 10, 't': 10},
                                'showactive': True,
                                'x': 0.17,
                                'xanchor': 'left',
                                'y': 1.2,
                                'yanchor': 'top'
                            }
                        ]
                    ))

    return fig

# Manual color change interaction
def manual_color_change(G, node_colors):
    """
    Simulates manual color changes on the map and checks whether the Four-Color Theorem holds.
    """
    while True:
        node = int(input("Enter region number to change color (1-N): ")) - 1
        print("Select a color: 0=Red, 1=Blue, 2=Green, 3=Yellow")
        color = int(input("Enter color number: "))
        
        if node in G.nodes:
            node_colors[node] = color
            
            # Validate the coloring
            for neighbor in G.neighbors(node):
                if node_colors[neighbor] == color:
                    print(f"Invalid! Region {node + 1} shares the same color with its neighbor Region {neighbor + 1}.")
                    break
            else:
                print(f"Region {node + 1} is now {color_names[color]}.")

        fig = plot_map(G, node_colors)
        fig.show()

# Function to assign initial valid colors
def assign_colors(G):
    """
    Assign colors to the graph using the four-color theorem.
    Ensures no two adjacent nodes share the same color.
    """
    color_map = nx.coloring.greedy_color(G, strategy="largest_first")
    
    # Convert to a color format (using the predefined 4 colors)
    node_colors = []
    for node in G.nodes():
        node_colors.append(color_map[node] % len(colors))  # Ensuring 4 colors max
    
    return node_colors

# Main execution
if __name__ == "__main__":
    num_nodes = 10  # You can modify the number of regions
    edge_probability = 0.4  # The probability that two regions are adjacent
    G = create_complex_map(num_nodes, edge_probability)  # Create a random map graph

    node_colors = assign_colors(G)  # Assign initial valid colors to regions
    fig = plot_map(G, node_colors)  # Plot the map with initial coloring
    fig.show()  # Display the initial graph

    # Allow the user to manually change colors and validate the theorem
    manual_color_change(G, node_colors)
