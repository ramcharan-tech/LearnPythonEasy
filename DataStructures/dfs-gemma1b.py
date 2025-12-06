def iterative_dfs(graph, start_node):
    """
    Performs Depth-First Search on a graph using an iterative stack.

    Args:
        graph: A dictionary representing the graph. Keys are nodes, 
               values are lists of their neighbors.
        start_node: The node to start the search from.

    Returns:
        A list of nodes visited in DFS order.
    """
    visited = set()  # Use a set for efficient membership checking
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()  # LIFO (Last-In, First-Out)
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add neighbors to the stack in reverse order to maintain DFS order
            neighbors = graph.get(node, [])  # Handle nodes with no neighbors
            for neighbor in reversed(neighbors):  # Reverse for DFS order
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

# Example Graph (Dictionary representation)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
dfs_result = iterative_dfs(graph, start_node)
print(f"DFS traversal starting from {start_node}: {dfs_result}")