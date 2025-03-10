F-> A full binary tree is a binary tree with either zero or two child nodes for each node. L = I + 1
C-> A complete binary tree is a special type of binary tree where all the levels of the tree are filled completely except the lowest level nodes which are filled from as left as possible. For the creation of a Complete Binary Tree, we require a queue data structure to keep track of the inserted nodes. Applied in heap sort.
P-> A perfect binary tree is a special type of binary tree in which all the leaf nodes are at the same depth, and all non-leaf nodes have two children. depth of n has 2^n leaf nodes and a total of 2^(n+1) – 1 nodes
B->Balanced Binary tree--> A binary tree is considered height-balanced if the absolute difference in heights of the left and right subtrees is at most 1 for every node in the tree
T-> A Ternary Tree is a tree data structure in which each node has at most three child nodes, usually distinguished as “left”, “mid” and “right”.
N-ary Tree (Generic Tree)--> Generic trees are a collection of nodes where each node is a data structure that consists of records and a list of references to its children(duplicate references are not allowed)
Also refer Degenerate Binary Tree

## Based on nodes values:
- **Binary Search Tree**:  A binary Search Tree is a node-based binary tree data structure that has the following properties:

>   The left subtree of a node contains only nodes with keys lesser than the node’s key.\
  The right subtree of a node contains only nodes with keys greater than the node’s key.\
  The left and right subtree each must also be a binary search tree.
- **AVL tree** is a self-balancing BST where the difference between heights of left and right subtrees for any node cannot be more than one.
- **red-black tree** is a kind of self-balancing BST where each node has an extra bit, and that bit is often interpreted as the color (red or black). These colors are used to ensure that the tree remains balanced during insertions and deletions. 
  > Every node has a color either red or black.
The root of the tree is always black.\
There are no two adjacent red nodes (A red node cannot have a red parent or red child).\
Every path from a node (including root) to any of its descendants’ NULL nodes has the same number of black nodes.\
All leaf (NULL) nodes are black nodes.
- **B-Tree** is a self-balancing search tree. In most of the other self-balancing search trees (like AVL and Red-Black Trees), it is assumed that everything is in the main memory. 
  > Properties of B-Tree: 
All leaves are at the same level.\
B-Tree is defined by the term minimum degree ‘t‘. The value of ‘t‘ depends upon disk block size.\
Every node except the root must contain at least t-1 keys. The root may contain a minimum of 1 key.\
All nodes (including root) may contain at most (2*t – 1) keys.\
The number of children of a node is equal to the number of keys in it plus 1.\
All keys of a node are sorted in increasing order. The child between two keys k1 and k2 contains all keys in the range from k1 and k2.\
B-Tree grows and shrinks from the root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward.\
Like other balanced Binary Search Trees, the time complexity to search, insert and delete is O(log n).\
Insertion of a Node in B-Tree happens only at Leaf Node.
- **B+ tree** eliminates the drawback B-tree used for indexing by storing data pointers only at the leaf nodes of the tree. Thus, the structure of leaf nodes of a B+ tree is quite different from the structure of internal nodes of the B tree.
-  **Segment Tree**, also known as a statistic tree, is a tree data structure used for storing information about intervals, or segments. It allows querying which of the stored segments contain a given point. It is, in principle, a static structure; that is, it’s a structure that cannot be modified once it’s built. A similar data structure is the interval tree.