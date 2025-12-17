
# properties

- n nodes have n-1 edges
- depth of a node = number of edges from root to that given node
- height of tree = max number of edges from root to leaf
- degree = number of children

# uses

- dom, dns, folder structure, b+- indexing in databases, bst - fast,search,insert,delete, find closest item, heap tree- implement priority queues, syntax tree - scanning,parsing,evaluatte arthmetic operations, trie - implement dictionaries with prefix lookup, suffix - pattern searching
- chess game store defense moves of a player
- decision making algo's in AI
- provides sorted data and searching floor and ceiling of data

# traversals
- Inorder = l -> root -> r (inorder for bst -> sorted array)
- preorder = root -> l -> r (used in expression trees to generate prefix notation)
- postorder = l -> r -> root (used for tree deletion because subtrees are deleted from the current node, postfix expression generation)
- level order (breadth first search) = maintain lists of list of level nodes or using queue
- queue implementation algo steps = corner case or base case --> declare q,res --> initialize with first value --> while q --> for len(q)
