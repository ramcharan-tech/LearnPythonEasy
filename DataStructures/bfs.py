from collections import deque

def bfs(graph,start):
    q = deque([start])
    visited = set({start})
    while q:
        n = q.popleft()
        print(n,end=" ")
        for v in graph[n]:
            if v not in visited:
                visited.add(v)
                q.append(v)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A') #start the bfs from node A.