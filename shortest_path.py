my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph, start, target=""):
    """
    Calculate the shortest path from a start node to a target node in a graph.

    Parameters:
    - graph (dict): A dictionary representation of the graph where keys are node names, and values are lists of tuples (connected node, distance).
    - start (str): The starting node for the path calculation.
    - target (str, optional): The target node for which the shortest path is to be found. If empty, paths to all nodes from start will be calculated.

    Returns:
    tuple: A tuple containing two dictionaries:
    - distances: A dictionary with nodes as keys and their shortest distance from the start node as values.
    - paths: A dictionary with nodes as keys and the list representing the shortest path from the start node as values.
    """
    # Initialize the list of unvisited nodes.
    unvisited = list(graph)
    # Initialize distances from the start node to all other nodes with infinity, except for the start node itself which is 0.
    distances = {node: 0 if node == start else float("inf") for node in graph}
    # Initialize paths dictionary to track the shortest path to each node.
    paths = {node: [] for node in graph}
    # Set the path from the start node to itself.
    paths[start].append(start)
    # Loop until all nodes have been visited.
    while unvisited:
        # Select the unvisited node with the smallest distance from the start node.
        current = min(unvisited, key=distances.get)
        # Update the distances and paths for all adjacent nodes.
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                # Update the path if a new shortest path is found.
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        # Mark the current node as visited.
        unvisited.remove(current)
    # Print the distance and path to the target node(s).
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )
    return distances, paths


shortest_path(my_graph, "A", "F")
