from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Step 1: Standard DFS to store nodes in stack by finish time
    def _dfs_fill_order(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_fill_order(neighbor, visited, stack)
        # Push to stack when all neighbors are visited (Finish Time)
        stack.append(v)

    # Function to get the Transpose (Reversed) Graph
    def _get_transpose(self):
        g_t = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g_t.add_edge(j, i) # Reverse direction: u->v becomes v->u
        return g_t

    # Step 3: DFS on the Transposed Graph
    def _dfs_print_scc(self, v, visited, current_component):
        visited[v] = True
        current_component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_print_scc(neighbor, visited, current_component)

    # Main function to find and print SCCs
    def print_sccs(self):
        stack = []
        visited = [False] * self.V

        # 1. Fill stack based on finishing times
        for i in range(self.V):
            if not visited[i]:
                self._dfs_fill_order(i, visited, stack)

        # 2. Create a reversed graph
        gr = self._get_transpose()

        # 3. Process all vertices in order defined by stack
        visited = [False] * self.V
        sccs = []
        
        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gr._dfs_print_scc(i, visited, component)
                sccs.append(component)
        
        return sccs

# --- Example Usage ---
if __name__ == "__main__":
    # Create a graph with 5 vertices (0 to 4)
    g = Graph(5)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0) # 0-1-2 forms a cycle (SCC)
    g.add_edge(0, 3)
    g.add_edge(3, 4) # 3 goes to 4, but 4 cannot go back

    print("Strongly Connected Components:")
    results = g.print_sccs()
    
    for idx, scc in enumerate(results):
        print(f"Component {idx + 1}: {scc}")