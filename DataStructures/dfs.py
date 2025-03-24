# DFS(node):
#     Mark node as visited
#     Process node (e.g., print or store it)
#     For each neighbor of node:
#         If neighbor is not visited:
#             DFS(neighbor)

# DFS(start_node):
#     Create an empty stack
#     Push start_node onto the stack
#     While stack is not empty:
#         Pop a node from the stack
#         If node is not visited:
#             Mark node as visited
#             Process node
#             Push all unvisited neighbors of node onto the stack