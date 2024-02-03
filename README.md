# Shortest Path

This Python script calculates the shortest path from a starting node to a target node within a graph. It utilizes Dijkstra's algorithm to find the shortest paths from the start node to all other nodes in the graph if a specific target node is not provided.

## Features

- **Graph Definition**: Allows defining directed graphs with weights.
- **Flexible Targeting**: Calculate the shortest path to a specific node or to all nodes from a starting point.
- **Path and Distance Output**: Provides both the shortest distance and the actual path taken to reach the target node(s).

## How to Use

1. **Define Your Graph**: The graph should be a dictionary where each key is a node, and each value is a list of tuples. Each tuple represents a connection to another node and the distance to that node. For example:

```python
my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}
```

2. **Run the Shortest Path Calculation**: Use the `shortest_path` function by specifying your graph, the starting node, and optionally the target node. If no target is specified, it calculates the shortest paths to all nodes.

```python
shortest_path(my_graph, "A", "F")
```

3. **Review the Output**: The function prints the shortest distance and path from the start node to the target node(s). It also returns two dictionaries containing the distances and paths for further use or analysis.

## Function Parameters

- `graph (dict)`: The graph represented as a dictionary.
- `start (str)`: The starting node for the path calculation.
- `target (str, optional)`: The target node for the shortest path calculation. If left empty, the function calculates paths to all nodes.

## Returns

- `tuple`: A tuple containing two dictionaries:
  - `distances`: Nodes as keys and their shortest distance from the start node as values.
  - `paths`: Nodes as keys and the list representing the shortest path from the start node as values.

## Example Output

For a call like `shortest_path(my_graph, "A", "F")`, the output could be:

```
A-F distance: 8
Path: A -> B -> F
```

This indicates that the shortest path from node A to node F has a distance of 8, passing through nodes A, B, and then F.

## Requirements

This script requires Python 3.x. No external libraries are needed.