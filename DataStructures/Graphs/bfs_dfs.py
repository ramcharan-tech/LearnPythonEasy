from collections import deque
def bfs(adj):
    src, V, res= 0, len(adj), []
    q = deque(src)
    visited = [False] * V
    visited[src] = True
    while q:
        curr = q.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                
    print(res)

def dfs(adj):
    src, V, res= 0, len(adj), []
    stk = [src]
    visited = [False] * V

    while stk:
        curr = stk.pop()
        if not visited[curr]:
            visited[curr] = True
            res.append(curr)

        for i in reversed(adj[curr]):
            if not visited[i]:
                stk.append(i)
    print(res)

def dfsrec(adj, node, visited, res):
    visited[node] = True
    res.append(node)

    for i in adj[node]:
        if not visited[i]:
            dfsrec(adj, i, visited, res)
    return res


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    # Number of vertices
    V = 6
    # Adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    # Adding edges
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 0)
    addEdge(adj, 0, 3)
    addEdge(adj, 5, 4)
    dfs(adj)

    # Printing the adjacency list
    for i in range(V):
        print(f"{i}: {adj[i]}")
    