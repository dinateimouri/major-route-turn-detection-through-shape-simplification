import matplotlib.pyplot as plt
import networkx as nx


def plot_path_dce(digraph, path, path_dce, plot_name):
    # Original path
    path_edges = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
    g = nx.DiGraph()
    g.add_edges_from(path_edges)
    positions = {n_id: (digraph.nodes[n_id]['lon'], digraph.nodes[n_id]['lat']) for n_id in path}
    nodes_color = ['none']
    edges_color = ['r']
    fig, ax = plt.subplots(figsize=(16, 16))
    nx.draw_networkx(g, positions, node_color=nodes_color, node_size=500, edge_color=edges_color, width=3,
                     arrowsize=10, with_labels=False, ax=ax)

    # Evolved path
    path_dce_edges = [(path_dce[n], path_dce[n + 1]) for n in range(len(path_dce) - 1)]
    g2 = nx.DiGraph()
    g2.add_edges_from(path_dce_edges)
    nodes_color = ['none']
    edges_color = ['g']
    positions = {n_id: (digraph.nodes[n_id]['lon'], digraph.nodes[n_id]['lat']) for n_id in path_dce}
    nx.draw_networkx(g2, positions, node_color=nodes_color, node_size=500, edge_color=edges_color, width=3,
                     arrowsize=10, with_labels=False, ax=ax)
    plt.savefig(plot_name)
    plt.close()


def plot_current_shape(digraph, current_shape, plot_name):
    current_shape_edges = [(current_shape[n], current_shape[n + 1]) for n in range(len(current_shape) - 1)]
    g = nx.DiGraph()
    g.add_edges_from(current_shape_edges)
    positions = {n_id: [digraph.nodes[n_id]['lon'], digraph.nodes[n_id]['lat']] for n_id in current_shape}
    fig, ax = plt.subplots(figsize=(10, 10))
    nx.draw_networkx(g, positions, node_size=0, width=2, arrows=False, edge_color='k', ax=ax)
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Current Shape')
    fig.savefig(plot_name)
    plt.close(fig)

    return
