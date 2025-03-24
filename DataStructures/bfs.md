```python
from collections import deque

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search (BFS) on a graph.

    Args:
        graph: A dictionary representing the graph.  Keys are nodes, and values are lists of their neighbors.
               Example: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
        start_node: The node to start the BFS from.

    Returns:
        A list containing the nodes visited in BFS order.  If the graph is not connected, it will only traverse
        the component containing the start_node.
    """

    visited = set()  # Keep track of visited nodes to avoid cycles
    queue = deque([start_node]) # Use a deque for efficient FIFO operations
    bfs_traversal = [] # Store the nodes in the order they are visited

    visited.add(start_node) # Mark the start node as visited

    while queue:
        node = queue.popleft()  # Get the next node from the queue (FIFO)
        bfs_traversal.append(node) # Add the node to the traversal order

        for neighbor in graph[node]:  # Iterate through the neighbors of the current node
            if neighbor not in visited:  # Check if the neighbor has been visited
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Add the neighbor to the queue

    return bfs_traversal


# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
bfs_result = bfs(graph, start_node)
print(f"BFS Traversal starting from node {start_node}: {bfs_result}")  # Output: ['A', 'B', 'C', 'D', 'E', 'F']


# Example with a disconnected graph:
disconnected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
    'E': ['F'],  # Disconnected from the rest of the graph
    'F': ['E']
}

start_node = 'A'
bfs_result = bfs(disconnected_graph, start_node)
print(f"BFS Traversal (disconnected graph) starting from node {start_node}: {bfs_result}") # Output: ['A', 'B', 'C', 'D']

start_node = 'E'
bfs_result = bfs(disconnected_graph, start_node)
print(f"BFS Traversal (disconnected graph) starting from node {start_node}: {bfs_result}") # Output: ['E', 'F']
```

**Explanation:**

1. **`bfs(graph, start_node)` Function:**
   - Takes a `graph` (represented as a dictionary where keys are nodes and values are lists of neighbors) and a `start_node` as input.
   - Returns a list containing the nodes visited in the BFS order.

2. **Initialization:**
   - `visited = set()`: Creates an empty set called `visited` to keep track of the nodes that have already been visited. Using a `set` provides efficient checking for membership (checking if a node is in the `visited` set).
   - `queue = deque([start_node])`:  Creates a `deque` (double-ended queue) from the `collections` module. A `deque` is used because it allows efficient insertion and deletion from both ends, which is crucial for BFS (FIFO - First-In, First-Out). The queue is initialized with the `start_node`.
   - `bfs_traversal = []`: Creates an empty list `bfs_traversal` to store the nodes in the order they are visited by the BFS algorithm.

3. **Mark the Start Node:**
   - `visited.add(start_node)`: Marks the `start_node` as visited by adding it to the `visited` set. This prevents the algorithm from revisiting the start node immediately.

4. **Main Loop:**
   - `while queue:`: The `while` loop continues as long as the `queue` is not empty.  This means there are still nodes to explore.
   - `node = queue.popleft()`:  Removes and returns the element at the left end of the `queue` (FIFO behavior). This is the next node to be processed.
   - `bfs_traversal.append(node)`:  Adds the current `node` to the `bfs_traversal` list, recording the order of visitation.
   - `for neighbor in graph[node]:`: Iterates through the neighbors of the current `node`. The neighbors are retrieved from the `graph` dictionary using `graph[node]`.
   - `if neighbor not in visited:`: Checks if the `neighbor` has already been visited. If it's not in the `visited` set, it means it's an unvisited node.
     - `visited.add(neighbor)`: Marks the `neighbor` as visited by adding it to the `visited` set.
     - `queue.append(neighbor)`: Adds the `neighbor` to the right end of the `queue`.  This ensures that the neighbor will be explored later, following the BFS principle of exploring all nodes at the current level before moving to the next level.

5. **Return Result:**
   - `return bfs_traversal`: After the `while` loop finishes (when the `queue` is empty, meaning all reachable nodes have been visited), the function returns the `bfs_traversal` list, which contains the nodes visited in BFS order.

**Key Concepts and How BFS Works:**

* **Breadth-First:** BFS explores the graph layer by layer. It visits all the immediate neighbors of a node before moving on to their neighbors.  This "breadth" is achieved through the use of a queue.
* **FIFO (First-In, First-Out) Queue:**  The queue is the heart of BFS.  Nodes are added to the *end* of the queue and removed from the *beginning*.  This ensures that nodes at the same distance from the starting node are visited in the order they were discovered.
* **Visited Set:** The `visited` set is crucial to prevent infinite loops in graphs with cycles.  Without it, the algorithm could repeatedly visit the same nodes, leading to an endless loop.
* **Graph Representation:** The example uses a dictionary where keys are nodes and values are lists of neighbors. This is a common way to represent graphs in code.  Alternatives include adjacency matrices.
* **Connected Components:** If the graph is disconnected (meaning there are parts of the graph that are not reachable from the starting node), BFS will only traverse the connected component containing the `start_node`.  The disconnected graph example demonstrates this.

**Why BFS is Useful:**

* **Shortest Path in Unweighted Graphs:** BFS finds the shortest path between two nodes in an *unweighted* graph (where all edges have the same "cost"). The number of edges in the BFS path from the start node to any other node is the shortest distance.
* **Level Order Traversal:** It's often used for level order traversal of trees.
* **Network Routing:**  Used in some network routing algorithms.
* **Web Crawling:**  Can be used to explore a website by visiting all its pages in a breadth-first manner.

**Time and Space Complexity:**

* **Time Complexity:** O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph. This is because BFS visits each vertex and edge at most once.
* **Space Complexity:** O(V), in the worst case.  This is because the `queue` and `visited` set could potentially store all the vertices of the graph.